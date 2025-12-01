##############################################################################
# Register custom blocks
##############################################################################
from sdg_hub.core.blocks.base import BaseBlock
from sdg_hub.core.blocks.llm.llm_chat_block import LLMChatBlock
from sdg_hub.core.blocks.registry import BlockRegistry
from pydantic import ConfigDict, field_validator
import validators
from sdg_hub.core.utils.logger_config import setup_logger
from litellm import acompletion, completion
import pandas as pd
from typing import Any, Optional
import asyncio
logger = setup_logger(__name__)
import os

@BlockRegistry.register("CustomLLMMultimodalBlock", 
                        "llm", 
                        "Extension of BaseBlock that supports multimodal models")
class CustomLLMMultimodalBlock(LLMChatBlock):
    """Extends LLMChatBlock to support multimodal models"""

    model_config = ConfigDict(extra="allow")

    def monkey_patch_messages(self, records):
        """Adds <image_url> message to the list of existing messages"""

        for i, record in enumerate(records):
            
            image_url = None
    
            user = list(filter(lambda x: x["role"]=="user", record))[0]        
                
            _, _, image_url = user["content"].partition("```image_url: ")
        
            if not validators.url(image_url):
    
                raise ValueError(f"Error processing image_url: Ensure image_url={image_url} is valid")
                
            user["content"] = [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                        "detail": "high",
                    },
                },
                {
                    "type": "text",
                    "text": "Extract the data from the image",
                },
            ]

        return records

    def _generate_sync(
        self,
        messages_list: list[list[dict[str, Any]]],
        completion_kwargs: dict[str, Any],
    ) -> list[list[dict[str, Any]]]:
        """Generate responses synchronously.

        Parameters
        ----------
        messages_list : list[list[dict[str, Any]]]
            List of message lists to process.
        completion_kwargs : dict[str, Any]
            Kwargs for LiteLLM completion.

        Returns
        -------
        list[list[dict[str, Any]]]
            List of response lists, each containing LiteLLM completion response dictionaries.
        """

        logger = setup_logger(__name__)
        
        responses = []

        messages_list = self.monkey_patch_messages(messages_list)

        for i, messages in enumerate(messages_list):
            try:
                response = completion(messages=messages, **completion_kwargs)
                # Extract response based on n parameter
                n_value = completion_kwargs.get("n", 1)
                if n_value > 1:
                    response_data = [
                        self._message_to_dict(choice.message)
                        for choice in response.choices
                    ]
                else:
                    response_data = [self._message_to_dict(response.choices[0].message)]
                responses.append(response_data)

                # Log progress for large batches
                if (i + 1) % 10 == 0:
                    logger.debug(
                        "Generated %d/%d responses",
                        i + 1,
                        len(messages_list),
                        extra={
                            "block_name": self.block_name,
                            "progress": f"{i + 1}/{len(messages_list)}",
                        },
                    )

            except Exception as e:
                logger.error(
                    "Failed to generate response for sample %d: %s",
                    i,
                    str(e),
                    extra={
                        "block_name": self.block_name,
                        "sample_index": i,
                        "error": str(e),
                    },
                )
                raise

        return responses

    async def _generate_async(
        self,
        messages_list: list[list[dict[str, Any]]],
        completion_kwargs: dict[str, Any],
        flow_max_concurrency: Optional[int] = None,
    ) -> list[list[dict[str, Any]]]:
        """Generate responses asynchronously.

        Parameters
        ----------
        messages_list : list[list[dict[str, Any]]]
            List of message lists to process.
        completion_kwargs : dict[str, Any]
            Kwargs for LiteLLM acompletion.
        flow_max_concurrency : Optional[int], optional
            Maximum concurrency for async requests.

        Returns
        -------
        list[list[dict[str, Any]]]
            List of response lists, each containing LiteLLM completion response dictionaries.
        """

        try:

            logger = setup_logger(__name__)

            messages_list = self.monkey_patch_messages(messages_list)
            
            if flow_max_concurrency is not None:
                # Validate max_concurrency parameter
                if flow_max_concurrency < 1:
                    raise ValueError(
                        f"max_concurrency must be greater than 0, got {flow_max_concurrency}"
                    )

                # Adjust concurrency based on n parameter (number of completions per request)
                effective_concurrency = flow_max_concurrency
                n_value = completion_kwargs.get("n", 1)

                if n_value and n_value > 1:
                    if flow_max_concurrency >= n_value:
                        # Adjust concurrency to account for n completions per request
                        effective_concurrency = flow_max_concurrency // n_value
                        logger.debug(
                            "Adjusted max_concurrency from %d to %d for n=%d completions per request",
                            flow_max_concurrency,
                            effective_concurrency,
                            n_value,
                            extra={
                                "block_name": self.block_name,
                                "original_max_concurrency": flow_max_concurrency,
                                "adjusted_max_concurrency": effective_concurrency,
                                "n_value": n_value,
                            },
                        )
                    else:
                        # Warn when max_concurrency is less than n
                        logger.warning(
                            "max_concurrency (%d) is less than n (%d). Consider increasing max_concurrency for optimal performance.",
                            flow_max_concurrency,
                            n_value,
                            extra={
                                "block_name": self.block_name,
                                "max_concurrency": flow_max_concurrency,
                                "n_value": n_value,
                            },
                        )
                        effective_concurrency = flow_max_concurrency

                # Use semaphore for concurrency control
                semaphore = asyncio.Semaphore(effective_concurrency)
                tasks = [
                    self._make_acompletion(messages, completion_kwargs, semaphore)
                    for messages in messages_list
                ]
            else:
                # No concurrency limit
                tasks = [
                    self._make_acompletion(messages, completion_kwargs)
                    for messages in messages_list
                ]

            responses = await asyncio.gather(*tasks)
            return responses

        except Exception as e:
            logger.error(
                "Failed to generate async responses: %s",
                str(e),
                extra={
                    "block_name": self.block_name,
                    "batch_size": len(messages_list),
                    "error": str(e),
                },
            )
            raise


@BlockRegistry.register(
    "CustomDeleteColumnsBlock",
    "transform",
    "Drops columns in a dataset",
)
class CustomDeleteColumnsBlock(BaseBlock):
    """Block for dropping columns in a dataset.

    Attributes
    ----------
    block_name : str
        Name of the block.
    input_cols
    """

    @field_validator("input_cols", mode="after")
    @classmethod
    def validate_input_cols(cls, v):
        """Validate that input_cols is a non-empty dict."""
        if not v:
            raise ValueError("input_cols cannot be empty")
        return v

    def generate(self, samples: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """Generate a dataset with dropped columns.

        Parameters
        ----------
        samples : pd.DataFrame
            Input dataset from which columns will be dropped.

        Returns
        -------
        pd.DataFrame
            Dataset with dropped columns.

        Raises
        ------
        ValueError
            If attempting to drop a column that don't exist in the dataset.
        """
        # Check that all original column names exist in the dataset
        existing_cols = set(samples.columns.tolist())
        droppable_cols = set(self.input_cols)

        missing_cols = droppable_cols - existing_cols
        if missing_cols:
            raise ValueError(
                f"Droppable column names {sorted(missing_cols)} not in the dataset"
            )

        # Drop columns using pandas method
        return samples.drop(columns=self.input_cols)
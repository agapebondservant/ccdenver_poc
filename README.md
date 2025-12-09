# County and City of Denver POC

## Set up custom workbenches
The following workbenches were used:
- Custom Agentic Workbench (LangGraph): <a href="https://quay.io/repository/oawofolurh/agentic-wb" target="_blank">Workbench Image</a>
- Custom GraphRAG Workbench: <a href="https://quay.io/repository/oawofolurh/graphrag-wb" target="_blank">Workbench Image</a>

- Use the generated wb-secret.yaml file below to set up the 
Environment variables for the workbenches (under "Environment Variables" 
section, select Variable Type -> Upload, then upload the generated file below):
```
oc delete secret data-prep-wb --ignore-not-found
oc create secret generic data-prep-wb --from-env-file .env
oc get secret data-prep-wb -oyaml > wb-secret.yaml
```

## Deploy LLMs
### Deploy the baseline model
Run the following (use the following settings as guidance):
```
# Gemma3-27b quantized
python -m vllm.entrypoints.openai.api_server \
--model gemma3-27b-quant \
--dtype=auto
--max_model_len=4096
--gpu_memory_utilization=0.9
--enable_chunked_prefill
--trust_remote_code
--enforce-eager

# IBM Granite-4-Tiny
python -m vllm.entrypoints.openai.api_server \
--model ibm-granite/granite-4.0-h-tiny \
--dtype bfloat16 \
--max-model-len 128000 \
--trust-remote-code \
--gpu-memory-utilization 0.9
```


## Build demo app
See app/README.md


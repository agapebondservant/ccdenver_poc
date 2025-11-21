##############################################################################
# Crews
##############################################################################

from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Optional
from pydantic import Field, BaseModel
from crewai_tools import SerperDevTool
from crewai.tools import tool
import os

##############################################################################
# LLMs
##############################################################################

main_llm = LLM(
    
    model=os.getenv('LLAMASCOUT4_LLM_NAME'),
    
    api_key=os.getenv('LLAMASCOUT4_LLM_KEY'),
    
    base_url=os.getenv('LLAMASCOUT4_LLM_BASE'),

    max_tokens = 8192,
)

##############################################################################
# Structured Output
##############################################################################

class DriversLicenseField(BaseModel):
    
    field: str = Field("", description="Name of field")
    
    error_reason: str = Field("", description="Reason for invalid or missing field")

    is_valid: Optional[bool] = Field(None, description="Indicates whether the entity is currently active.")

class DriversLicenseMetadata(BaseModel):
    
    name: DriversLicenseField = Field(description="Name of driver's license owner")
    
    date_of_birth: DriversLicenseField = Field(description="Date of birth of driver's license owner")
    
    expiration_date: DriversLicenseField = Field(description="Expiration date of driver's license")
    
    state_issued: DriversLicenseField = Field(description="State where the license was issued")


@CrewBase
class ValidateDriversLicense():
    """Given a driver's license, extracts relevant metadata and validates it against a provided application profile."""

    agents: List[BaseAgent]
    
    tasks: List[Task]
        
    @agent
    def quality_assurance_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance_specialist'],
            
            verbose=False,
            
            llm=main_llm,
        )
            
    @task
    def quality_assurance_specialist_task(self) -> Task:
        return Task(
            config=self.tasks_config["quality_assurance_specialist"], 
        )
        
    @agent
    def content_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_reviewer'],
            
            verbose=False,
            
            llm=main_llm,
        )
            
    @task
    def content_reviewer_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_reviewer"], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ValidateDriversLicense crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
        )
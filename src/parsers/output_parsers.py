from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class PersonSummary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="Interesting facts about the person")


person_summary_parser = PydanticOutputParser(pydantic_object=PersonSummary)

from typing import Tuple

from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

from src.agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from src.connectors.linkedin import scrape_linkedin_profile
from src.parsers.output_parsers import person_summary_parser, PersonSummary

load_dotenv()


def ice_breaker_with(name: str) -> Tuple[PersonSummary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    # Use mock false for real scrape
    linkedin_data = scrape_linkedin_profile(profile_url=linkedin_url, mock=True)
    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. three interesting fact about them
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_summary_parser.get_format_instructions()
        },
    )
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | person_summary_parser
    res = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Ice Breaker:")
    print(ice_breaker_with(name="Alec Hantson"))

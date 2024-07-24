from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

from src.agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from src.connectors.linkedin import scrape_linkedin_profile

load_dotenv()


def ice_breaker_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    # Use mock false for real scrape
    linkedin_data = scrape_linkedin_profile(profile_url=linkedin_url, mock=True)
    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. two interesting fact about them
    """
    summary_prompt_template = PromptTemplate(template=summary_template)
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_data})
    return res


if __name__ == "__main__":
    print("Ice Breaker:")
    print(ice_breaker_with(name="Alec Hantson"))

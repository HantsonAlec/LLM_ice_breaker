from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

from connectors.linkedin import scrape_linkedin_profile

load_dotenv()


if __name__ == "__main__":
    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. two interesting fact about them
    """
    summary_prompt_template = PromptTemplate(template=summary_template)
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    # llm = ChatOllama(model='mistral')

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(profile_url="mock_url", mock=True)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)

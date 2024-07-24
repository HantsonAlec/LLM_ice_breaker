from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from src.tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOllama(model="mistral", temperature=0)

    template = """given the full name {name_of_person} I want you to get me a lnk to their LinkedIn profile page.
    Your answer should contain only a URL."""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    agent_tools = [
        Tool(
            name="Crawl google for linkedIn profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the LinkedIn profile page url",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=agent_tools, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=agent_tools, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Alec Hantson")

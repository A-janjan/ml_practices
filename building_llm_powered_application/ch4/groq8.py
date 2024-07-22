import os
from dotenv import load_dotenv
from langchain import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import AzureChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
# Import Azure OpenAI
from langchain.llms import AzureOpenAI
from langchain.schema import HumanMessage

model = AzureChatOpenAI(
    deployment_name='gpt-3.5-turbo',
    openai_api_type="azure",
)

model(
    [
        HumanMessage(
            content="Translate this sentence from English to French. I love programming."
        )
    ]
)

load_dotenv()

key = os.environ["SERPAPI_API_KEY"]

search = SerpAPIWrapper()
tools = [
    Tool.from_function(
        func=search.run,
        name="Search",
        description="useful for when you need to answer questions about current events"
    )
    ]

agent_executor = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


print(agent_executor.agent.llm_chain.prompt.template)


agent_executor('who are going to be the italian male athletes for climbing at the Paris 2024 Olympics?')


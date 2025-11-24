from typing import Any
from langchain.agents import create_agent
from toolbox.tools import get_latest_price, get_company_news

async def get_chat_completion(message: str) -> str:
    """
    Generate a chat completion using tools and agents.
    """

    text = message.strip()
    if not text:
        return ""
    
    tools = [get_latest_price, get_company_news]
    agent = create_agent(
        "gpt-4o",
        tools,
    )

    result: Any = agent.invoke({"messages": [{"role": "user", "content": text}]})

    return result["messages"][-1].content
from typing import Any
from langchain.agents import create_agent
from toolbox.tools import (
    get_price_history,
    get_company_news,
    get_earnings_history,
    get_earnings_estimates,
    get_upgrades_downgrades,
    get_analyst_price_targets,
    get_info
)

async def get_chat_completion(message: str) -> str:
    """
    Generate a chat completion using tools and agents.
    """

    text = message.strip()
    if not text:
        return ""
    
    tools = [
        get_price_history,
        get_company_news,
        get_earnings_history,
        get_earnings_estimates,
        get_upgrades_downgrades,
        get_analyst_price_targets,
        get_info
    ]
    agent = create_agent(
        "gpt-4o",
        tools,
    )

    result: Any = agent.invoke({"messages": [{"role": "user", "content": text}]})

    return result["messages"][-1].content
from typing import Any
import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from toolbox.tools import (
    get_price_history,
    get_company_news,
    get_earnings_history,
    get_earnings_estimates,
    get_upgrades_downgrades,
    get_analyst_price_targets,
    get_info,
)


def _build_chat_model() -> ChatOpenAI:
    """Construct the base chat model used by the agent.

    Centralizing this makes it easy to tweak the model name,
    temperature, or other settings in one place. The model name
    is read from the ``MODEL_NAME`` environment variable with a
    sensible default.
    """

    model_name = os.getenv("MODEL_NAME", "gpt-4.1-mini")

    return ChatOpenAI(
        model=model_name,
        temperature=0.1,
    )


async def get_chat_completion(message: str) -> str:
    """Generate a chat completion using the configured agent and tools."""

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
        get_info,
    ]

    llm = _build_chat_model()
    agent = create_agent(llm, tools)

    system_prompt = (
        "You are Market Bot, a helpful financial research assistant. "
        "Answer questions about stocks, ETFs, crypto, macro trends, and "
        "trading ideas using only the information available from your tools "
        "and general financial knowledge. Be concise, avoid speculation you "
        "cannot justify, and highlight uncertainty when data is limited. "
        "Always respond in Markdown, using headings, lists, and tables when helpful."
        "When you output tables, use standard Markdown table formatting."
        "Note:"
        "Do not add additional commentary like mentioning potential inaccuracies."
        "Do not make up data; just state that you don't have that information."
        "Do not ask user if they want more information, only provide concise answers."
    )

    result: Any = agent.invoke(
        {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ]
        }
    )

    return result["messages"][-1].content
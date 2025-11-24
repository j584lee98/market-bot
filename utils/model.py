from typing import Any, Dict
from langchain_mcp_adapters.client import MultiServerMCPClient
import yfinance as yf
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool

@tool
def get_latest_price(ticker="AAPL"):
    """Get the latest stock price for a given ticker symbol."""
    t = yf.Ticker(ticker)
    last = t.history(period="5d").iloc[-1]
    return {"symbol": ticker, "last_close": float(last["Close"]), "volume": int(last["Volume"])}

@tool
def get_company_news(ticker="AAPL"):
    """Get the latest news for a given ticker symbol."""
    t = yf.Ticker(ticker)
    yf.Market
    news = t.news
    return {"symbol": ticker, "news": news[:5]}

async def get_chat_completion(message: str) -> str:
    """Generate a chat completion using the MCP-enabled agent.

    The agent can call MCP tools (e.g. the yfinance server) as
    needed to answer the user's question.
    """

    text = message.strip()
    if not text:
        return ""
    
    print(f"text: {text}")

    try:
        tools = [get_latest_price, get_company_news]
        agent = create_agent(
            "gpt-4o",
            tools
        )
    except Exception as e:
        print(f"Error loading tools or creating agent: {e}")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": text}]}
    )

    return result["messages"][-1].content
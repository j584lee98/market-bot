from typing import Dict, Any
import yfinance as yf
from langchain.tools import tool

@tool
def get_latest_price(
    ticker: str,
    period: str = "1mo",
    interval: str = "1d",
    start: str | None = None,
    end: str | None = None,
) -> Dict[str, Any]:
    """
    Get historical price data for a ticker.

    Args:
        ticker: Symbol such as "AAPL".
        period: Valid periods - 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max.
        interval: Valid intervals - 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo.
        start: Optional start date ("YYYY-MM-DD").
        end: Optional end date ("YYYY-MM-DD").

    Returns:
        A dict showing historical price data.
    """

    t = yf.Ticker(ticker)
    history = t.history(period=period, interval=interval, start=start, end=end)
    return history.to_dict()

@tool
def get_company_news(ticker: str, count: int = 5) -> Dict[str, Any]:
    """
    Get recent news items for a ticker.

    Args:
        ticker: Symbol such as "AAPL".
        count: Maximum number of news items to retrieve.

    Returns:
        A list of recent news items.
    """

    t = yf.Ticker(ticker)
    news = t.get_news(count)
    return news

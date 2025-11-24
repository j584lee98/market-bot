from typing import Any, Dict

import yfinance as yf
from langchain.tools import tool


@tool
def get_price_history(
    ticker: str,
    period: str = "1mo",
    interval: str = "1d",
    start: str | None = None,
    end: str | None = None,
) -> Dict[str, Any]:
    """Get historical OHLCV, dividends, and stock splits data for a ticker.

    This tool is best when the question is about how a stock has
    traded over time (trends, volatility, drawdowns, etc.).

    Args:
        ticker: Symbol such as "AAPL".
        period: History period, e.g. "1d", "5d", "1mo", "6mo", "1y".
        interval: Bar interval, e.g. "1m", "5m", "1h", "1d".
        start: Optional start date in "YYYY-MM-DD" format.
        end: Optional end date in "YYYY-MM-DD" format.

    Returns:
        A list of OHLCV, dividend, and stock split records with timestamps.
    """

    t = yf.Ticker(ticker)
    history = t.history(period=period, interval=interval, start=start, end=end)
    return history.to_dict(orient="records")


@tool
def get_company_news(ticker: str, count: int = 5) -> Dict[str, Any]:
    """Get recent news items for a ticker.

    Use this when the question is about headlines, catalysts,
    or qualitative events affecting the stock.

    Args:
        ticker: Symbol such as "AAPL".
        count: Maximum number of news items to retrieve.

    Returns:
        A list of news items for ticker.
    """

    t = yf.Ticker(ticker)
    news = t.get_news(count)
    return news


@tool
def get_earnings_history(ticker: str) -> Dict[str, Any]:
    """Get past earnings dates and results for a ticker.

    This is useful when the question is about how the company has
    performed around previous earnings announcements.

    Args:
        ticker: Symbol such as "AAPL".

    Returns:
        A list of earnings records with dates and reported values.
    """

    t = yf.Ticker(ticker)
    earnings = t.get_earnings_dates()
    return earnings.to_dict(orient="records")


@tool
def get_earnings_estimates(ticker: str) -> Dict[str, Any]:
    """Get upcoming earnings calendar / estimates for a ticker.

    Use this when the question is about the next earnings date or
    expectations around upcoming reports.

    Args:
        ticker: Symbol such as "AAPL".

    Returns:
        A dict describing the earnings calendar.
    """

    t = yf.Ticker(ticker)
    estimates = t.get_calendar()
    return estimates


@tool
def get_upgrades_downgrades(ticker: str) -> Dict[str, Any]:
    """Get analyst upgrades and downgrades for a ticker.

    Use this when the question is about analyst opinion changes
    (rating changes, new coverage, etc.).

    Args:
        ticker: Symbol such as "AAPL".

    Returns:
        A list of analyst rating update records.
    """

    t = yf.Ticker(ticker)
    updates = t.get_upgrades_downgrades()
    return updates.to_dict(orient="records")


@tool
def get_analyst_price_targets(ticker: str) -> Dict[str, Any]:
    """Get analyst price targets and related stats for a ticker.

    This is useful when the question involves upside / downside
    to consensus target price or analyst ranges.

    Args:
        ticker: Symbol such as "AAPL".

    Returns:
        A dict with price target statistics and details.
    """

    t = yf.Ticker(ticker)
    targets = t.get_analyst_price_targets()
    return targets


@tool
def get_info(ticker: str) -> Dict[str, Any]:
    """Get a broad set of fundamental and descriptive data.

    This tool returns a detailed collection of fields about the
    company (name, sector, industry, market cap, valuation ratios,
    balance-sheet and income-statement style metrics, and more).

    If none of the more specific tools (price history, news,
    earnings, analyst ratings/targets) fit the user question,
    prefer calling this tool as a general "company snapshot" source.

    Args:
        ticker: Symbol such as "AAPL".

    Returns:
        A dict of general company information and key metrics.
    """

    t = yf.Ticker(ticker)
    info = t.get_info()
    return info
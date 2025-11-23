import datetime as _dt
from typing import Any, Dict, List, Optional
import yfinance as yf
from mcp.server.fastmcp import FastMCP

"""MCP server exposing basic market data via yfinance.

Tools are intentionally simple so they can be composed inside an LLM chain.
"""

mcp = FastMCP("yfinance")


def _normalize_ticker(ticker: str) -> str:
	"""Normalize ticker input (strip and uppercase)."""
	return ticker.strip().upper()


@mcp.tool()
def get_current_price(ticker: str) -> Dict[str, Any]:
	"""Get the latest market price for a symbol.

	Args:
		ticker: Symbol such as "AAPL", "MSFT", or "SPY".

	Returns:
		A dict with the latest price and currency, if available.
	"""

	symbol = _normalize_ticker(ticker)
	info: Dict[str, Any] = {}

	try:
		t = yf.Ticker(symbol)
		# fast path: use .fast_info if available
		if hasattr(t, "fast_info") and t.fast_info is not None:
			info = dict(t.fast_info)
			price = info.get("last_price") or info.get("regular_market_price")
			currency = info.get("currency") or info.get("quote_currency")
		else:
			hist = t.history(period="1d")
			price = float(hist["Close"].iloc[-1]) if not hist.empty else None
			currency = None

		return {
			"ticker": symbol,
			"price": price,
			"currency": currency,
		}
	except Exception as exc:  # keep errors surfaced in a structured way
		return {
			"ticker": symbol,
			"error": str(exc),
		}


@mcp.tool()
def get_history(
	ticker: str,
	period: str = "1mo",
	interval: str = "1d",
	include_volume: bool = False,
) -> Dict[str, Any]:
	"""Get historical OHLC data for a symbol using yfinance.

	Args:
		ticker: Symbol such as "AAPL".
		period: yfinance period string (e.g. "1d", "5d", "1mo", "3mo", "1y").
		interval: yfinance interval (e.g. "1m", "5m", "15m", "1h", "1d").
		include_volume: Whether to include volume in the response.

	Returns:
		A dict with a simplified list of candle records.
	"""

	symbol = _normalize_ticker(ticker)

	try:
		t = yf.Ticker(symbol)
		df = t.history(period=period, interval=interval)

		if df.empty:
			return {"ticker": symbol, "candles": [], "note": "No data"}

		candles: List[Dict[str, Any]] = []
		for ts, row in df.iterrows():
			candle: Dict[str, Any] = {
				"timestamp": ts.isoformat() if isinstance(ts, _dt.datetime) else str(ts),
				"open": float(row["Open"]),
				"high": float(row["High"]),
				"low": float(row["Low"]),
				"close": float(row["Close"]),
			}
			if include_volume and "Volume" in row:
				candle["volume"] = int(row["Volume"]) if not _dt.isaware else row["Volume"]
			candles.append(candle)

		return {
			"ticker": symbol,
			"period": period,
			"interval": interval,
			"candles": candles,
		}
	except Exception as exc:
		return {
			"ticker": symbol,
			"error": str(exc),
		}


@mcp.tool()
def get_summary(ticker: str) -> Dict[str, Optional[Any]]:
	"""Get a high-level summary for a symbol (name, sector, market cap, etc.).

	This is useful for the LLM to enrich responses with basic company metadata.
	"""

	symbol = _normalize_ticker(ticker)

	try:
		t = yf.Ticker(symbol)
		info = t.info or {}
		return {
			"ticker": symbol,
			"shortName": info.get("shortName"),
			"longName": info.get("longName"),
			"sector": info.get("sector"),
			"industry": info.get("industry"),
			"currency": info.get("currency"),
			"marketCap": info.get("marketCap"),
			"fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
			"fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
		}
	except Exception as exc:
		return {
			"ticker": symbol,
			"error": str(exc),
		}

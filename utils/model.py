"""Model utilities for the Market Bot API.

This module is responsible for constructing the LLM (and, later,
any MCP-integrated tools/agents).  The FastAPI chat endpoint imports
and calls the `get_chat_completion` coroutine from here so all model
logic is centralized in one place.
"""

from __future__ import annotations

import os
from typing import Any, Dict

from openai import OpenAI

# Single shared OpenAI client for the process.
_client: OpenAI | None = None


def _get_openai_client() -> OpenAI:
    """Return a singleton OpenAI client instance.

    This keeps connection management in one place and makes it easy to
    later swap in a different provider or add MCP tooling.
    """

    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        _client = OpenAI(api_key=api_key)
    return _client


async def get_chat_completion(message: str) -> str:
    """Generate a chat completion for a single user message.

    This is the function the FastAPI endpoint calls.  For now it uses
    OpenAI's Chat Completions API directly; you can later extend this to
    route via LangChain + MCP tools if desired.
    """

    text = message.strip()
    if not text:
        return ""

    client = _get_openai_client()

    # The OpenAI Python SDK is sync; run it in a thread when awaited
    # from async contexts if needed.  Here we call it directly and
    # return the result as an async function.
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )

    return completion.choices[0].message.content if completion.choices else ""

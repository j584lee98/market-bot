from typing import Any, Dict, Mapping, Optional
from langchain.agents import create_agent
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient

MCPServerConfig = Mapping[str, Mapping[str, Any]]

async def create_mcp_client(servers: MCPServerConfig) -> MultiServerMCPClient:
    """Create and initialize a :class:`MultiServerMCPClient`.

    Parameters
    ----------
    servers:
        A mapping from server name to configuration, e.g.::

            {
                "math": {
                    "transport": "stdio",
                    "command": "python",
                    "args": ["/path/to/mcp_server.py"],
                }
            }

    Returns
    -------
    MultiServerMCPClient
        The initialized client, ready to be used with LangChain.
    """

    client = MultiServerMCPClient(servers)
    # Ensure all MCP servers are connected and tools are fetched lazily.
    await client.await_startup()
    return client


async def create_mcp_agent(
    model: str,
    client: MultiServerMCPClient,
    *,
    model_kwargs: Optional[Dict[str, Any]] = None,
) -> Any:
    """Create a LangChain agent that can call MCP tools.

    Parameters
    ----------
    model:
        Model name for the underlying chat model (e.g. "gpt-4o").
    client:
        A started :class:`MultiServerMCPClient` instance.
    model_kwargs:
        Optional extra keyword arguments to pass to the chat model
        constructor (temperature, max_tokens, etc.).

    Returns
    -------
    AgentExecutor compatible object
        The value returned by :func:`langchain.agents.create_agent`.
    """

    _model_kwargs: Dict[str, Any] = {"model": model}
    if model_kwargs:
        _model_kwargs.update(model_kwargs)

    llm: BaseChatModel = ChatOpenAI(**_model_kwargs)

    tools = await client.get_tools()
    agent = create_agent(llm, tools)
    return agent

"""MCP server for alloyfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from alloyfyi.api import AlloyFYI

mcp = FastMCP("alloyfyi")


@mcp.tool()
def search_alloyfyi(query: str) -> dict[str, Any]:
    """Search alloyfyi.com for content matching the query."""
    with AlloyFYI() as api:
        return api.search(query)

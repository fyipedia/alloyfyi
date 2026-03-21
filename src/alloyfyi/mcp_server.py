"""MCP server for alloyfyi — AI assistant tools for alloyfyi.com.

Run: uvx --from "alloyfyi[mcp]" python -m alloyfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AlloyFYI")


@mcp.tool()
def list_alloys(limit: int = 20, offset: int = 0) -> str:
    """List alloys from alloyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from alloyfyi.api import AlloyFYI

    with AlloyFYI() as api:
        data = api.list_alloys(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No alloys found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_alloy(slug: str) -> str:
    """Get detailed information about a specific alloy.

    Args:
        slug: URL slug identifier for the alloy.
    """
    from alloyfyi.api import AlloyFYI

    with AlloyFYI() as api:
        data = api.get_alloy(slug)
        return str(data)


@mcp.tool()
def list_families(limit: int = 20, offset: int = 0) -> str:
    """List families from alloyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from alloyfyi.api import AlloyFYI

    with AlloyFYI() as api:
        data = api.list_families(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No families found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_alloy(query: str) -> str:
    """Search alloyfyi.com for metal alloys, compositions, and properties.

    Args:
        query: Search query string.
    """
    from alloyfyi.api import AlloyFYI

    with AlloyFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()

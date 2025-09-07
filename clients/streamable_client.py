"""
source: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#writing-mcp-clients
Run from the repository root:
    uv run clients/streamable_client.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            for tool in tools.tools:
                print("=" * 40, "\n")
                print(
                    f"Tool Name: {tool.name}\n"
                    f"Description: {tool.description}\n"
                    f"Input Schema: {tool.inputSchema}\n"
                    f"Title: {tool.title}\n"
                )
                print("=" * 40, "\n")
            # Example: call the 'greet' tool
            result = await session.call_tool("greet", {"name": "world!"})
            print("result: ", result)


if __name__ == "__main__":
    asyncio.run(main())

"""
source: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#writing-mcp-clients
Run from the repository root:
    uv run clients/stdio_client.py
"""

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

server_params = StdioServerParameters(
    command="uv",
    args=["run", "servers/stdio_servers/calculator.py"],
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialise session
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            for tool in tools.tools:
                print("=" * 40, "\n")
                print(
                    f"Tool Name: {tool.name}\n"
                    f"Description: {tool.description}\n"
                    f"Input Schema: {tool.inputSchema}\n"
                    f"Output Schema: {tool.outputSchema}\n"
                    f"Title: {tool.title}\n"
                )
                print("=" * 40, "\n")
            # Example: call the 'add' tool
            result = await session.call_tool("add", {"a": 5, "b": 3})
            print("Add result:", result)


if __name__ == "__main__":
    asyncio.run(run())

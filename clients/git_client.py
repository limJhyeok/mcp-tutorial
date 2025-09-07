from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import os

server_params = StdioServerParameters(
    command="uvx",
    args=[
        "mcp-server-git",
        "--repository",
        os.getcwd(),
    ],
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
                    f"Title: {tool.title}\n"
                )
                print("=" * 40, "\n")

                result = await session.call_tool(
                    "git_status", {"repo_path": os.getcwd()}
                )
                print("Add result:", result)


if __name__ == "__main__":
    asyncio.run(run())

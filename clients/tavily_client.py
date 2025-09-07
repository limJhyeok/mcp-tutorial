from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

server_params = StdioServerParameters(
    command="npx",
    args=["-y", "tavily-mcp@latest"],
    env={"TAVILY_API_KEY": TAVILY_API_KEY},
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

            # call serach tool
            tool_name = "tavily-search"
            arguments = {"query": "latest AI research papers 2025"}
            result = await session.call_tool(tool_name, arguments)
            print(result)


if __name__ == "__main__":
    asyncio.run(run())

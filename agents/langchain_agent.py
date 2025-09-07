from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import json
import asyncio
import os
from dotenv import load_dotenv
import logging
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()


async def start_chat_session(agent):
    config = RunnableConfig(
        configurable={"thread_id": "1"},
    )  # support multi turn

    while True:
        try:
            user_input = input("You: ").strip().lower()
            if user_input in ["quit", "exit"]:
                logging.info("\nExiting...")
                break
            response = await agent.ainvoke(
                {"messages": [("user", user_input)]}, config=config
            )

            ai_message = response["messages"][-1]
            ai_content = ai_message.content
            logging.info("\nAssistant: %s", ai_content)

        except KeyboardInterrupt:
            logging.info("\nExiting...")
            break


async def main():
    server_config_path = "langchain_server_config.json"
    with open(server_config_path, "r") as f:
        server_config = json.load(f)

    mcp_client_args = {}
    for name, srv_config in server_config["mcpServers"].items():
        if srv_config.get("env"):
            srv_config["env"] = {**os.environ}
        mcp_client_args[name] = srv_config
    client = MultiServerMCPClient(mcp_client_args)

    tools = await client.get_tools()
    memory = MemorySaver()  # support multi turn

    agent = create_react_agent("openai:gpt-4.1", tools=tools, checkpointer=memory)

    await start_chat_session(agent)


if __name__ == "__main__":
    asyncio.run(main())

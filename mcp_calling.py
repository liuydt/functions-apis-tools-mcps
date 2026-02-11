import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

load_dotenv()


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "Weather Station MCP": {
                "transport": "http",
                "url": "http://127.0.0.1:8000/mcp",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatOpenAI(
        model="gpt-5-nano",
        temperature=0.1,
        timeout=30,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    agent = create_agent(model, tools=tools)

    query = "What's the weather like in London?"
    response = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})

    messages = response.get("messages", [])
    if messages:
        print(messages[-1].content)
    else:
        print(response)


if __name__ == "__main__":
    asyncio.run(main())

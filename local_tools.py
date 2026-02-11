from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

from weather_station_tools import get_current_weather, get_wind_speed, get_humidity

def main() -> None:
    model = ChatOpenAI(
        model="gpt-5-nano",
        temperature=0.1,
        timeout=30,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    agent = create_agent(model, tools=[get_current_weather, get_wind_speed, get_humidity])

    query = "What's the weather like in London?"
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})

    messages = response.get("messages", [])
    if messages:
        print(messages[-1].content)
    else:
        print(response)

    print("=======================================")

    query = "is it windy in London?"
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})

    messages = response.get("messages", [])
    if messages:
        print(messages[-1].content)
    else:
        print(response)


if __name__ == "__main__":
    main()

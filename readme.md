# API vs MCP

This project is to demon the differences among local function calls, API calls, local agent tools and MCP servers.

## General steps to create a new project

1. Create python virtual environment, in terminal

`python -m venv .venv`

2. Activate virtual environment, in terminal

for MacOS,
`source .venv/bin/activate`

for Windows,
`.venv\Scripts\activate`

3. install required packages.

popular package managers are: pip and uv. 

4. (Optinal) manage environment viables by python-dotenv

`pip install python-dotenv`

in your code, use the following to load environment viables defined in .env file.

`from dotenv import load_dotenv`
`load_dotenv()`

5. (Optinal) Version control

### Local function

functions are defined in weather_station.py
local_function.py uses these functions.

in terminal, run
`python local_cunction.py`

### APIs

we can use fastapi to turn local functions to APIs.
APIs are defined in weather_station_api.py

in terminal, run `fastapi dev weather_station_api.py` to run APIs in API server. 

At this stage, APIs can be accessed in browser.

We can also use code to access APIs. examples are in api_call.py.

### LLM with local tools.

Tools are defined in weather_station_tools.py

How to use tools are shown in local_tools.py

For AI Agents, we don't need to explicitely call the function like in local functions or API calls.

LLM will decide to call which tool(function).

### LLM with MCP servers.

We use FastMCP to create a local MCP server.

How to use the tools provided by MCP server are shown in mcp_calling.py

AI agent will find all the available tools provided by the MCP server.

LLM will decide to call which tool(function).
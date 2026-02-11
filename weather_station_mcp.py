from fastmcp import FastMCP

mcp = FastMCP("Weather Station MCP")

@mcp.tool("get_current_weather")
def get_current_weather(city: str) -> str:
    """Get the current weather in a given location
    
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: A string describing the current weather in the specified city.
    """
    # Placeholder for actual weather fetching logic

    print(f"Fetching weather for {city} From Weather Station MCP...")  # Debug statement to trace function calls
    return f"From local tool: The current weather in {city} is sunny with a temperature of 25°C."

@mcp.tool("get_wind_speed")
def get_wind_speed(city: str) -> str:
    """Get the current wind speed in a given location
    
    Args:        
        city (str): The name of the city to get the wind speed for.
    Returns:
        str: A string describing the current wind speed in the specified city.
    """
    # Placeholder for actual wind speed fetching logic
    print(f"Fetching wind speed for {city} From Weather Station MCP...")  # Debug statement to trace function calls
    return f"From local tool: The current wind speed in {city} is 15 km/h."

@mcp.tool("get_humidity")
def get_humidity(city: str) -> str:     
    """Get the current humidity in a given location

    Args:
        city (str): The name of the city to get the humidity for.
    Returns:
        str: A string describing the current humidity in the specified city.
    """
    # Placeholder for actual humidity fetching logic
    print(f"Fetching humidity for {city} From Weather Station MCP...")  # Debug statement to trace function calls
    return f"From local tool: The current humidity in {city} is 60%."

if __name__ == "__main__":
    mcp.run(transport="http")
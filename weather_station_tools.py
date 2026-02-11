from langchain.tools import tool

@tool("get_current_weather")
def get_current_weather(city: str) -> str:
    """Get the current weather in a given location
    
    Args:
        city (str): The name of the city to get the weather for.
    Returns:
        str: A string describing the current weather in the specified city.
    """
    # Placeholder for actual weather fetching logic

    print(f"Fetching weather for {city}...")  # Debug statement to trace function calls
    return f"From local tool: The current weather in {city} is sunny with a temperature of 25°C."

@tool("get_wind_speed")
def get_wind_speed(city: str) -> str:
    """Get the current wind speed in a given location
    
    Args:        
        city (str): The name of the city to get the wind speed for.
    Returns:
        str: A string describing the current wind speed in the specified city.
    """
    # Placeholder for actual wind speed fetching logic
    print(f"Fetching wind speed for {city}...")  # Debug statement to trace function calls
    return f"From local tool: The current wind speed in {city} is 15 km/h."

@tool("get_humicity")
def get_humicity(city: str) -> str:     
    """Get the current humicity in a given location

    Args:
        city (str): The name of the city to get the humicity for.
    Returns:
        str: A string describing the current humicity in the specified city.
    """
    # Placeholder for actual humicity fetching logic
    print(f"Fetching humicity for {city}...")  # Debug statement to trace function calls
    return f"From local tool: The current humicity in {city} is 60%."
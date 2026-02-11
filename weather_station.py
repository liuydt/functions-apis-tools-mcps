class WeatherStation:
    def __init__(self, name: str):
        self.name = name

    def get_weather(self, city: str) -> str:
        # Placeholder for actual weather fetching logic
        return f"The current weather in {city} is sunny with a temperature of 25°C."
    
    def get_wind_speed(self, city: str) -> str:
        # Placeholder for actual wind speed fetching logic
        return f"The current wind speed in {city} is 15 km/h."
    
    def get_humidity(self, city: str) -> str:
        # Placeholder for actual humidity fetching logic
        return f"The current humidity in {city} is 60%."
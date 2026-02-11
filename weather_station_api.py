from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Weather Station API"}

@app.get("/weather/{city}")
def get_weather(city: str):
    # Placeholder for actual weather fetching logic
    return {"city": city, "weather": f"From Weather Station API: The current weather in {city} is sunny with a temperature of 25°C."}

@app.get("/wind_speed/{city}")
def get_wind_speed(city: str):
    # Placeholder for actual wind speed fetching logic
    return {"city": city, "wind_speed": f"From Weather Station API: The current wind speed in {city} is 15 km/h."}

@app.get("/humidity/{city}")
def get_humidity(city: str):
    # Placeholder for actual humidity fetching logic
    return {"city": city, "humidity": f"From Weather Station API: The current humidity in {city} is 60%."}
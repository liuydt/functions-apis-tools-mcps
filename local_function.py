from weather_station import WeatherStation

# if I want to do some 'magic' thing, I probably need to define a function like this:
def generate_response(query: str) -> str:
    station = WeatherStation("My Weather Station")
    city = "London"
    
    if "weather" in query:
        return station.get_weather(city)
    elif "wind speed" in query:
        return station.get_wind_speed(city)
    elif "humidity" in query:
        return station.get_humidity(city)
    else:
        return "Sorry, I don't understand the query."

def main():
    station = WeatherStation("My Weather Station")
    city = "London"
    
    # How to call the local functions.
    print(station.get_weather(city))
    print(station.get_wind_speed(city))
    print(station.get_humidity(city))

    query = "What's the weather like in London?"
    response = generate_response(query)
    print(response)

    query = "Which city is UK's Capital?"
    response = generate_response(query)
    print(response)

if __name__ == "__main__":
    main()
import json
from urllib import error, parse, request

BASE_URL = "http://127.0.0.1:8000"


def _call_weather_api(endpoint: str, city: str) -> str:
    url = f"{BASE_URL}/{endpoint}/{city}"

    try:
        with request.urlopen(url, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except error.URLError as exc:
        return f"API request failed: {exc}"
    except json.JSONDecodeError:
        return "API returned an invalid JSON response."

    if endpoint == "weather":
        return payload.get("weather", "No weather data available.")
    if endpoint == "wind_speed":
        return payload.get("wind_speed", "No wind speed data available.")
    if endpoint == "humidity":
        return payload.get("humidity", "No humidity data available.")

    return "Unknown endpoint response."


# if I want to do some 'magic' thing, I probably need to define a function like this:
def generate_response(query: str) -> str:
    city = "London"
    lowered = query.lower()

    if "weather" in lowered:
        return _call_weather_api("weather", city)
    if "wind speed" in lowered:
        return _call_weather_api("wind_speed", city)
    if "humidity" in lowered:
        return _call_weather_api("humidity", city)

    return "Sorry, I don't understand the query."


def main() -> None:
    city = "London"

    # How to call the API endpoints.
    print(_call_weather_api("weather", city))
    print(_call_weather_api("wind_speed", city))
    print(_call_weather_api("humidity", city))

    query = "What's the weather like in London?"
    response = generate_response(query)
    print(response)

    query = "Which city is UK's Capital?"
    response = generate_response(query)
    print(response)


if __name__ == "__main__":
    main()

import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = '686089244d2de25a02aad24881dc95f3'
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def fetch_data(self,url):
        """
        Fetch data from the provided URL.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            dict or None: The data fetched from the URL in JSON format if the request was successful,
                        otherwise None.
        """
        try:
            response = requests.get(url)
            response.raise_for_status() # http error (no connection) etc
            data = response.json() #attempt to parse JSON
            return data
        except requests.exceptions.RequestException as e:
            print(f"Request Failed: {e}")
        except ValueError:
            print(f"Failed to decode JSON from response")     
            

    def fetch_weather_data(self, location):
        """
        Fetch current weather and forecast data for a given location.

        Args:
            api_key (str): The API key for authenticating with the OpenWeatherMap API.
            location (str): The location (city name) to fetch weather data for.

        Returns:
            tuple: A tuple containing two elements:
                - dict or None: The current weather data.
                - dict or None: The weather forecast data.
        """
        current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
        current_data = self.fetch_data(current_url)

        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
        forecast_data = self.fetch_data(forecast_url)

        return current_data, forecast_data

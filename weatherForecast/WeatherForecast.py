import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENWEATHERMAP_API_KEY')
city = 'Tokyo,jp'

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    forecast_data = response.json()
    print(json.dumps(forecast_data, indent=4))
else:
    print(f"Error fetching data from OpenWeatherMap API: Status Code {response.status_code}")
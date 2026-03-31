import argparse
import os
from dotenv import load_dotenv
load_dotenv()

import requests

api_key = os.getenv("API_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("--city", required=True, help="enter city name")
args = parser.parse_args()

city = args.city

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" #'&units=metric' to get temperature in Celsius

response = requests.get(url)

data = response.json()

if data.get("cod") != 200:
    print("city not found")
    exit()

#temp_c = data['main']['temp']-273.15 - to convert from Kelvin to Celsius

output = f"Weather in {city}: \n Temperature: {data['main']['temp']}°C \n Humidity: {data['main']['humidity']}% \n Description: {data['weather'][0]['description']}"
print(output)
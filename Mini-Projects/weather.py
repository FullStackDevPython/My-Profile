"""
Q3: Create a script called weather that return the environmental parameters (temperature
(min, max), windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you
want; after passing arguments (like user api and city id).
"""
# url = https://www.etutorialspoint.com/index.php/388-python-weather-api-script

# importing modules
import requests, json
from suntime import Sun
import datetime

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = input('Please enter the name of the city : ')

# Your API key
API_KEY = "Your-Key-Here"
def kelvin_to_celsius_fahrenheit(kelvin):
   celsius = kelvin - 273.15
   fahrenheit = celsius * (9/5) + 32
   return celsius, fahrenheit

def kelvin_to_celsius_fahrenheit_max(max_kelvin):
   celsius = max_kelvin - 273.15
   fahrenheit = celsius * (9/5) + 32
   return celsius, fahrenheit    

def kelvin_to_celsius_fahrenheit_min(min_kelvin):
   celsius = min_kelvin - 273.15
   fahrenheit = celsius * (9/5) + 32
   return celsius, fahrenheit   
# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
print(URL)
# Sending HTTP request
response = requests.get(URL).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
max_temp_kelvin = response['main']['temp_max']
max_temp_celsius, max_temp_fahrenheit = kelvin_to_celsius_fahrenheit_max(max_temp_kelvin)
min_temp_kelvin = response['main']['temp_min']
min_temp_celsius, min_temp_fahrenheit = kelvin_to_celsius_fahrenheit_min(min_temp_kelvin)

wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
pressure = response['main']['pressure']
description = response['weather'][0]['description']

sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
print(f"{CITY:-^35}")
print(f"Temperature in {CITY}: {temp_celsius:.2f}\N{DEGREE SIGN}C or {temp_fahrenheit:.2f}\N{DEGREE SIGN}F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}\N{DEGREE SIGN}C or {feels_like_fahrenheit:.2f}\N{DEGREE SIGN}F")
print(f"The Maximum Temperature in {CITY}: {max_temp_celsius:.2f}\N{DEGREE SIGN}C or {max_temp_fahrenheit:.2f}\N{DEGREE SIGN}F")
print(f"The Minimum Temperature in {CITY}: {min_temp_celsius:.2f}\N{DEGREE SIGN}C or {min_temp_fahrenheit:.2f}\N{DEGREE SIGN}F")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Clouds Condition in  {CITY}: {description}")
print(f"Pressure in {CITY}: {pressure}hPa")
print(f"Sun rises in {CITY}: {sunrise_time} local time")
print(f"Sun sets in {CITY}: {sunset_time} local time")
 

"""
OUTPUT :
Please enter the name of the city : Auckland
https://api.openweathermap.org/data/2.5/weather?q=Auckland&appid=490d7e630c37788bf37101c66b43833e
-------------Auckland--------------
Temperature in Auckland: 17.16°C or 62.89°F
Temperature in Auckland feels like: 16.73°C or 62.11°F
The Maximum Temperature in Auckland: 17.66°C or 63.79°F
The Minimum Temperature in Auckland: 15.97°C or 60.75°F
Wind Speed in Auckland: 1.54m/s
Humidity in Auckland: 69%
Clouds Condition in  Auckland: broken clouds
Pressure in Auckland: 1006hPa
Sun rises in Auckland: 2022-12-20 05:57:35 local time
Sun sets in Auckland: 2022-12-20 20:38:50 local time
"""
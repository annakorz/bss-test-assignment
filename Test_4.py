#  Написать программу на python, выводящую текущие данные о погоде с использованием 
# API сайта https://www.weatherbit.io/api
# Данные о погоде должны быть выведены в текстовом виде.

import requests as rq
import json

city_name = input("Enter the city name: ")
country_name = input("Enter the country code name (for example, RU, US, etc.): ")

API_KEY = '' # insert your API_KEY

def get_weather_from_weatherbit(city, country_abbreviation):
    """Function takes in strings with city name and country code and returns response from weatherbit website
    in JSON-format"""
    baseurl = "https://api.weatherbit.io/v2.0/current"
    params_d = {}
    params_d["city"] = city
    params_d["country"] = country_abbreviation
    params_d["key"] = API_KEY
    weatherbit_resp = rq.get(baseurl, params=params_d)

    return weatherbit_resp.json()


def extract_info(weather_d):
    """Function takes in a JSON-file and returns a dictionary with parsed data"""
    weather_data = {}
    weather_data["city"] = weather_d["data"][0]["city_name"]
    weather_data["country"] = weather_d["data"][0]["country_code"]
    weather_data["temp"] = weather_d["data"][0]["temp"]
    weather_data["description"] = weather_d["data"][0]["weather"]["description"]
    weather_data["sunrise"] = weather_d["data"][0]["sunrise"]
    weather_data["sunset"] = weather_d["data"][0]["sunset"]
    weather_data["wind_direction"] = weather_d["data"][0]["wind_cdir_full"]

    return weather_data

current_weather = extract_info(get_weather_from_weatherbit(city_name, country_name))
file_name = 'weather_forecast.txt'

with open(file_name, 'w') as file:
    print("Сохранение данных в файл...")
    file.write(f"In {current_weather['city']}, {current_weather['country']} \n {current_weather['temp']} degrees, \n {current_weather['description']}, \n {current_weather['wind_direction']} wind, \n sunrise at: {current_weather['sunrise']}, \n sunset at {current_weather['sunset']}.")
    print("Данные о погоде сохранены в файл {}".format(file_name))


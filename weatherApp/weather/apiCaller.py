#import certifi
import json
import urllib.parse
import urllib.request
from datetime import datetime
from . import Coordinate_Request
import time


API_KEY = '0b314396b7522fbd939166f3ed3e53a4'

BASE_URL ='https://api.darksky.net/forecast/'
#https://api.darksky.net/forecast/0b314396b7522fbd939166f3ed3e53a4/42.3601, -71.0589


def build_search_url(lat: float, lon: float):
    query_parameters= [('latitude', lat), ('longitude', lon)]
    return BASE_URL + API_KEY + "/" + str(query_parameters[0][1]) + "," + str(query_parameters[1][1])

def get_result(url:str):
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response!= None:
            response.close()


def pull_current_data(json_object):
    new_dict = {}
    new_dict['current_windSpeed'] = json_object['currently']['windSpeed']
    new_dict['current_humidity'] = json_object['currently']['humidity']
    new_dict['current_apparentTemperature'] = json_object['currently']['apparentTemperature']
    new_dict['current_temperature'] = json_object['currently']['temperature']
    new_dict['current_precipProbability'] = json_object['currently']['precipProbability']
    new_dict['current_summary'] = json_object['currently']['summary']
    new_dict['current_time'] = datetime.now()
    return new_dict

def pull_daily_data(json_object):
    daily_dict = {}
    daily_dict['daily_windSpeed'] = json_object['daily']['data'][0]['windSpeed']
    daily_dict['daily_humidity'] = json_object['daily']['data'][0]['humidity']
    daily_dict['daily_apparentTemperatureHigh'] = json_object['daily']['data'][0]['apparentTemperatureHigh']
    daily_dict['daily_apparentTemperatureLow'] = json_object['daily']['data'][0]['apparentTemperatureLow']
    daily_dict['daily_TemperatureLow'] = json_object['daily']['data'][0]['temperatureLow']
    daily_dict['daily_TemperatureHigh'] = json_object['daily']['data'][0]['temperatureHigh']
    daily_dict['daily_precipType'] = json_object['daily']['data'][0]['precipType']
    daily_dict['daily_precipProbability'] = json_object['daily']['data'][0]['precipProbability']
    sunrise = json_object['daily']['data'][0]['sunriseTime']
    sunrise1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sunrise))
    sunset = json_object['daily']['data'][0]['sunsetTime']
    sunset1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sunset))
    daily_dict['daily_sunriseTime'] = sunrise1
    daily_dict['daily_sunsetTime'] = sunset1
    daily_dict['daily_summary'] = json_object['daily']['data'][0]['summary']
    daily_dict['current_time'] = datetime.now()
    return daily_dict


def get_daily_dict():
    search_query = Coordinate_Request.run()
    result = pull_daily_data(get_result(build_search_url(search_query[0], search_query[1])))
    return result


def get_current_dict():
    search_query = Coordinate_Request.run()
    result = pull_current_data(get_result(build_search_url(search_query[0], search_query[1])))
    return result

if __name__ == "__main__":
    print(get_daily_dict())
    print(get_current_dict())

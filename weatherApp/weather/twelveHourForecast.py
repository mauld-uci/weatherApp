#12 hour forecast
import json
import time
from datetime import datetime
import urllib.parse
import urllib.request
import Coordinate_Request
from collections import namedtuple
HourWeather = namedtuple('Hour', ['time', 'human_time', 'timezone', 'summary', 'precipProbability', 'temperature', 'apparentTemperature',
                                  'humidity', 'windSpeed'])



API_KEY = '0b314396b7522fbd939166f3ed3e53a4'

BASE_URL ='https://api.darksky.net/forecast/'

'''
def format_time():
    seconds = time.time()
    local_time = time.ctime(seconds)
    split = local_time.split()
    days = {'Sat': '07', 'Sun': '01', 'Mon': '02', 'Tue': '03', 'Wed': '04', 'Thu':'05', 'Fri':'06' }
    months = {'Jan': '01,', 'Feb': '02', 'Mar':'03', 'Apr': '04', 'May': '05', 'Jun': '06',
              'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    year = split[-1]
    month = months[split[1]]
    day = split[2]
    hour = split[3][0:2]
    minute = split[3][3:5]
    second = split[3][6:8]
    time = "[{}]-[{}]-[{}]T[{}]:[{}]:[{}]".format(year, month, day, hour, minute, second)
    return time

'''
def build_search_url(lat: float, lon: float, time):
    query_parameters= [('latitude', lat), ('longitude', lon)]
    return BASE_URL + API_KEY + "/" + str(query_parameters[0][1]) + "," + str(query_parameters[1][1]) + "," + str(time)

def get_result(url:str):
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response!= None:
            response.close()

def generate_namedtuple_perHour(json_object):
    hour_tuple = HourWeather(time = json_object['currently']['time'],
                             human_time = str(datetime.now()),
                             timezone= json_object['timezone'],
                             summary= json_object['currently']['summary'],
                             precipProbability= json_object['currently']['precipProbability'],
                             temperature= json_object['currently']['temperature'],
                             apparentTemperature= json_object['currently']['apparentTemperature'],
                             humidity= json_object['currently']['humidity'],
                             windSpeed= json_object['currently']['windSpeed'])
    return hour_tuple

def pull_hour_data(lat, lon, time):
    url = build_search_url(lat, lon, time)
    response = get_result(url)
    return response


def hour_manager(current_time, lat, lon):
    twelve_hours = []
    time = current_time
    x = 0
    while x < 12:
        twelve_hours.append(generate_namedtuple_perHour(pull_hour_data(lat, lon, time)))
        time += 3600
        x += 1
    return twelve_hours

def run():
    search_query = Coordinate_Request.run()
    time1 = int(time.time())
    result = hour_manager(time1, search_query[0], search_query[1])
    return result


if __name__ == "__main__":
    print(run())

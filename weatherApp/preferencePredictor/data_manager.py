#data_manager.py

import math
import statistics
import weatherdata

class TemperatureData:
    def __init__(self):
        self.min = 400.0
        self.max = -400.0
        self.avg = 0.0
        self.stdev = 0.0
        self.length = 0
        self.data = []

    def add_data(data: weatherdata.WeatherData):
        temperature = data.temperature
        if temperature < self.min:
            self.min = temperature
        else if temperature > self.max:
            self.max = temperature
        length += 1
        avg = (avg*(length-1)+temperature)/length
        data.append(temperature)
        if length >= 2:
            self.stdev = stdev(data)

class HumidityData:
    def __init__(self):
        self.min = 1.0
        self.max = 0.0
        self.avg = 0.0
        self.stdev = 0.0
        self.length = 0.0
        self.data = []

    def add_data(data: weatherdata.WeatherData):
        humdity = data.humidity
        if humidity < self.min:
            self.min = humidity
        else if humidity > self.max:
            self.max = humidity
        length += 1
        avg = (avg*(length-1)+humidity)/length
        data.append(humidity)
        if length >= 2:
            self.stdev = stdev(data)

class PrecipitationData:
    def __init__(self):
        pass
    def add_data(data: weatherdata.WeatherData):
        pass

class WindData:
    def __init__(self):
        self.min = 0.0
        self.max = 200.0
        self.avg = 0.0
        self.stdev = 0.0
        self.length = 0.0
        self.data = []
    def add_data(data: weatherdata.WeatherData):
        wind_speed = data.wind
        if humidity < self.min:
            self.min = wind
        else if humidity > self.max:
            self.max = wind
        length += 1
        avg = (avg*(length-1)+wind)/length
        data.append(wind)
        if length >= 2:
            self.stdev = stdev(data)

class CloudData:
    def __init__(self):
        pass
    def add_data(data: weatherdata.WeatherData):
        pass

class SunData:
    def __init__(self):
        pass
    def add_data(data: weatherdata.WeatherData):
        pass

#################################
# REPLACE WITH DATABASE STORAGE #
#################################
temperature_list = [TemperatureData() for _ in range(5)]
apparent_list = [TemperatureData() for _ in range(5)]
humididty_list = [HumidityData()  for _ in range(5)]
precipitation_list = [PrecipitationData()  for _ in range(5)]
wind_list = [WindData()  for _ in range(5)]
cloud_list = [CloudData()  for _ in range(5)]
sun_list = [SunData()  for _ in range(5)]
#################################

def parse_data (data: weatherdata.WeatherData):
    '''
    Based on the feel index, decides whether to add data to database or compare
    '''
    feel_index = data.feel
    if feel_index == -1:
        comfort_level(data)
    elif 0 <= feel_index <= 4 :
        temperature_list[feel_index].add_data(data)
        apparent_list[feel_index].add_data(data)
        humididty_list[feel_index].add_data(data)
        precipitation_list[feel_index].add_data(data)
        wind_list[feel_index].add_data(data)
        cloud_list[feel_index].add_data(data)
        sun_list[feel_index].add_data(data)
    else:
        raise Exception("Invalid Feel Input")

def comfort_level (weatherdata.WeatherData):
    for td in temperature_list:
        stdevs_from_mean = []

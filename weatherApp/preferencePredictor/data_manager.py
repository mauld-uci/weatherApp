#data_manager.py

import math
import statistics
import weatherdata

class TemperatureData:
    def __init__(self):
        self.min = 400
        self.max = -400
        self.avg = 0
        self.stdev = 0
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

temperature_list = []


def add_data (data: weatherdata.WeatherData):
    feel_index = data.feel
    temperature_list[feel_index].add_data(data)


def comfort_level (weatherdata.WeatherData):

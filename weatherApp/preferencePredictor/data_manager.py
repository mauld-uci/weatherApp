#data_manager.py

import math
import statistics
import weatherdata

feel_index = {"freezing": 0, "cold": 1, "perfect": 2, "hot": 3, "burning": 4}
freezing_temp, cold_temp, perfect_temp, hot_temp, burning_temp = ([] for i in range(5))

data = []
temperature_data = []


def add_data_point(point : weatherdata.WeatherData) -> None:
    '''
    Adds a data point to the WeatherData array
    '''
    data.append(point)

    if point.feel == 0:
        freezing_temp.append(point.temperature)
    elif point.feel == 1:
        cold_temp.append(point.temperature)
    elif point.feel == 2:
        perfect_temp.append(point.temperature)
    elif point.feel == 3:
        hot_temp.append(point.temperature)
    elif point.feel == 4:
        burning_temp.append(point.temperature)

    print(freezing_temp)
    print(data)


def temperature_comfort(measured: float, data: [weatherdata.WeatherData]) -> int:
    '''
    Determines the comfort level (0-4) of the measured temperature
    '''
    

if __name__ == '__main__':
    while True:
        temp = input("Give a temperature: ")
        if (temp == '') : break
        temp = int(temp)
        feels = feel_index[input("Give a feeling: ")]
        add_data_point(weatherdata.WeatherData(feels, temp, 0, 0, 0, 0, 0, 0, 0))
    temperature_comfort(1.1111, data)

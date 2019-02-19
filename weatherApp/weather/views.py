# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
from . import apiCaller
from . import twelveHourForecast
from . import stats_analysis

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import UserDataPoint, WeatherData

weather_moods = {
    "-1": None,
    "0": "freezing!",
    "1": "a little chilly.",
    "2": "just right.",
    "3": "a bit warm.",
    "4": "burnin' hot."
}

weather_pics = {
    "-1": None,
    "0": "weather/svgGraphics/Freezing.svg",
    "1": "weather/svgGraphics/Chilly.svg",
    "2": "weather/svgGraphics/JustRightlogo.svg",
    "3": "weather/svgGraphics/Toastylogo.svg",
    "4": "weather/svgGraphics/OnFirelogo.svg"
}

appropriate_clothing = {
    "-1": None,
    "0": ["weather/svgGraphics/clothing/jacket.svg", "weather/svgGraphics/clothing/jacket.svg"],
    "1": ["weather/svgGraphics/clothing/jacket.svg", "weather/svgGraphics/clothing/longsleeve.svg"],
    "2": ["weather/svgGraphics/clothing/tshirt.svg", "weather/svgGraphics/clothing/longsleeve.svg"],
    "3": ["weather/svgGraphics/clothing/tshirt.svg", "weather/svgGraphics/clothing/sunglasses.svg"],
    "4": ["weather/svgGraphics/clothing/tanktop.svg", "weather/svgGraphics/clothing/sunglasses.svg"]
}

time_of_day_pics = {
    "day": "weather/svgGraphics/Sun.svg",
    "night": "weather/svgGraphics/Moon.svg"
}

def index(request):
    currentWeather = apiCaller.get_current_dict()
    dailyWeather = apiCaller.get_daily_dict()
    current_temp = currentWeather['current_temperature']

    hourly_forecast = twelveHourForecast.run()
    unzip_hourly = list(zip(*hourly_forecast))
    hours = change_from_military_time(unzip_hourly[0])
    hourly_temps = unzip_hourly[1]

    feeling_prediction = str(stats_analysis.find_closest_feeling(current_temp))

    if currentWeather['current_time'] >= dailyWeather['sunrise_time'] and currentWeather['current_time'] < dailyWeather['sunset_time']:
        time_of_day = "day"
    else:
        time_of_day = "night"

    context = {
        'current_temperature': current_temp,
        'current_wind_speed': currentWeather['current_windSpeed'],
        'feeling_prediction': weather_moods[feeling_prediction],
        'feeling_prediction_pic': weather_pics[feeling_prediction],
        'suggested_clothing_1': appropriate_clothing[feeling_prediction][0],
        'suggested_clothing_2': appropriate_clothing[feeling_prediction][1],
        'user_voted': True if 'user_voted' in request.session else False,
        'selected_choice': "-1" if 'selected_choice' not in request.session else request.session['selected_choice'],
        'user_data_count': UserDataPoint.objects.count(),
        'hours': hours,
        'hourly_temps': hourly_temps,
        'blurb': generate_blurb(currentWeather, dailyWeather, feeling_prediction),
        'time_of_day': time_of_day_pics[time_of_day]
    }
    context['weather_mood'] = weather_moods[context['selected_choice']]
    context['weather_pic'] = weather_pics[context['selected_choice']]

    return render(request, 'weather/index.html', context)

# def after_vote_redirect(request):
#     currentWeather = apiCaller.get_current_dict()

#     context = {
#         'current_temperature': currentWeather['current_temperature'],
#         'current_wind_speed': currentWeather['current_windSpeed'],
#         'user_voted': True,

#     }

#     return render(request, 'weather/index.html', context)

def comfortAsk(request):
    return render(request, 'weather/comfortAsk.html')

def submission(request):
    request_copy = request.POST.copy()
    try:
        request_copy.pop("csrfmiddlewaretoken")
        selected_choice = request_copy.popitem()[0]
        selected_choice = selected_choice[0]
        request.session['selected_choice'] = selected_choice
        request.session['user_voted'] = True
    except (KeyError):
        # Redisplay the ask form.
        return render(request, 'weather/comfortAsk.html', {
            'error_message': str(request.POST),
        })

    currentWeather = apiCaller.get_current_dict()
    dailyWeather = apiCaller.get_daily_dict()
    currentWeatherData = WeatherData(
        temperature = currentWeather['current_temperature'],
        apparent_temp = currentWeather['current_apparentTemperature'],
        humidity = currentWeather['current_humidity'],
        precip_prob = currentWeather['current_precipProbability'],
        windSpeed = currentWeather['current_windSpeed'],
        cloudiness = currentWeather['current_summary'],
        time = currentWeather['current_time'],
        sunrise = "2019-02-15 05:30" if 'daily_sunriseTime' not in dailyWeather else dailyWeather['daily_sunriseTime'],
        sunsetTime = "2019-02-15 05:30" if "daily_sunsetTime" not in dailyWeather else dailyWeather['daily_sunsetTime']
        #sunrise = dailyWeather['daily_sunriseTime'],
        #sunsetTime = dailyWeather['daily_sunsetTime']
    )

    currentWeatherData.save()
    dataPoint = UserDataPoint()
    dataPoint.feeling = int(request.session['selected_choice'])
    dataPoint.recordedWeather = currentWeatherData
    dataPoint.save()

    return HttpResponseRedirect(reverse('weather:index'))


def generate_blurb(currentWeather: dict, dailyWeather: dict, feel: str):
    currentWeather = apiCaller.get_current_dict()
    feel = int(feel)

    blurb = ''
    # hour_min_sec = currentWeather['current_time'].split(' ')[1].split(':')
    # time_in_min = int(hour_min_sec[0])*60 + int(hour_min_sec[1]) #0-1440 minutes
    # if 240 <= time_in_min < 720:
    #     blurb += "Good Morning! "
    # elif 720 <=  time_in_min < 1020:
    #     blurb += "Good Afternoon! "
    # elif 1020 <= time_in_min < 1440:
    #     blurb += "Good Evening! "
    # else:
    #     blurb += "Good Day! "

    blurb += "It's going to be "

    if feel == 0:
        blurb += "very cold "
    elif feel == 1:
        blurb += "a little chilly "
    elif feel == 2:
        blurb += "just how you like it "
    elif feel == 3:
        blurb += "a bit warm "
    elif feel == 4:
        blurb += "very hot "
    else:
        blurb += "magical "

    blurb += "outside today."

    if (dailyWeather['daily_summary']):
        blurb += " It will be raining today, so bring an umbrella! "
    if (dailyWeather['daily_precipProbability']):
        blurb += " It will be sunny out today, so bring your shades!"

    if (dailyWeather['daily_apparentTemperatureHigh'] > 90 and dailyWeather['daily_humidity'] >= 0.98):
        blurb += " Feels like a lawless swampland out today, so bring your guns!"
    if (dailyWeather['daily_apparentTemperatureHigh'] > 90 and dailyWeather['daily_windSpeed'] >= 30):
        blurb += " Hot and windy! Be careful Icarus!"
    if (dailyWeather['daily_apparentTemperatureHigh'] == 69 and dailyWeather['daily_humidity'] == .69):
        blurb += " Hehe."

    return blurb

def change_from_military_time(hours: tuple):
    hours_list = []
    for each in hours:
        newTime = ""
        if int(each) > 12:
            newTime = str(each-12) + 'pm'
        elif int(each) == 12:
            newTime = str(each) + 'pm'
        elif int(each) == 0:
            newTime = '12am'
        else:
            newTime = str(each) + 'am'
        hours_list.append(newTime)

    return hours_list


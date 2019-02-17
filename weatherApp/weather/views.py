# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
from . import apiCaller

from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import UserDataPoint, WeatherData


def index(request):
    currentWeather = apiCaller.get_current_dict()
    dailyWeather = apiCaller.get_daily_dict()
    feel = None #GET INPUT!!!!!!!

    blurb = ''
    hour_min_sec = currentWeather['CURRENT_TIME'].split(' ')[1].split(':')
    time_in_min = int(hour_min_sec[0])*60 + int(hour_min_sec[1]) #0-1440 minutes
    if 240 <= time_in_min < 720:
        blurb += "Good Morning! "
    elif 720 <= time_in_min < 1020:
        blurb += "Good Afternoon! "
    elif 1020 <= time_in_min < 1440:
        blurb += "Good Evening! "
    else
        blurb += "Good Day! "

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
    if (dailyWeather['daily_apparentTemperatureHigh'] == 69 and dailyWeather['daily_humidity'] == 69):
        blurb += " Hehe."

    return render(request, 'weather/index.html', currentWeather)

def comfortAsk(request):
    currentWeather = apiCaller.get_current_dict()
    currentWeatherData = WeatherData()
    dailyWeather = apiCaller.get_daily_dict()
    currentWeatherData.temperature = currentWeather['current_Temperature']
    currentWeatherData.apparentTemp = currentWeather['current_apparentTemperature']
    currentWeatherData.humidity = currentWeather['current_humidity']
    currentWeatherData.precip_prob = currentWeather['current_precipProbability']
    currentWeatherData.windSpeed = currentWeather['current_windSpeed']
    currentWeatherData.cloudiness = currentWeather['current_summary']
    currentWeatherData.time = currentWeather['CURRENT_TIME']
    currentWeatherData.sunrise = dailyWeather['daily_sunriseTime']
    currentWeatherData.sunsetTime = dailyWeather['daily_sunsetTime']
    dataPoint = UserDataPoint()
    # dataPoint.feeling = [SOME INPUT]
    # dataPoint.recordedWeather = currentWeatherData
    # dataPoint.save()
    return render(request, 'weather/comfortAsk.html')

# def vote(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'weather/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('weather:results', args=(question.id,)))

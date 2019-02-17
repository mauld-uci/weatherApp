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


def index(request, user_voted=False):
    currentWeather = apiCaller.get_current_dict()

    context = {
        'current_temperature': currentWeather['current_temperature'],
        'current_wind_speed': currentWeather['current_windSpeed'],
        'user_voted': user_voted,
    }

    return render(request, 'weather/index.html', context)

def comfortAsk(request):
    return render(request, 'weather/comfortAsk.html')

def submission(request):
    try:
        selected_choice = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the ask form.
        return render(request, 'weather/comfortAsk.html', {
            'error_message': "You didn't select a choice.",
        })


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

    return HttpResponseRedirect(reverse('', kwargs={user_voted: True}))



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

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
    
    return render(request, 'weather/index.html', currentWeather)

def comfortAsk(request):
    return render(request, 'weeather/comfortAsk.html')

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

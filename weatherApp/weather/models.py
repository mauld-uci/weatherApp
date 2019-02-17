# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class WeatherData(models.Model):
    temperature = models.IntegerField()
    apparent_temp = models.IntegerField()
    humidity = models.FloatField()
    precip_prob = models.FloatField()
    windSpeed = models.FloatField()
    cloudiness = models.CharField(max_length=30)
    time = models.DateTimeField()
    sunrise = models.DateTimeField()
    sunsetTime = models.DateTimeField()

class UserDataPoint(models.Model):
    feeling = models.IntegerField() #1-5
    recordedWeather = models.OneToOneField(WeatherData, on_delete=models.CASCADE)

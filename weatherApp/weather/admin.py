# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import UserDataPoint
from .models import WeatherData

admin.site.register(UserDataPoint)
admin.site.register(WeatherData)
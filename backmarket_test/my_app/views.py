# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from my_app.forms import CityForm
from api_client import API_Request
from weather import parse_weather


def home(request):
    """View rendering the home page. In case of a get, it will display a form 
    taking a name of the city the user wants infos on. In case of post, it 
    will display weather forecast informations"""

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"].lower()
            api_client = API_Request(city)
            woeid = api_client.woeid

            # Checking the api find a city
            if woeid:
                weather = api_client.get_weather()

                city = parse_weather(weather).city
                country = parse_weather(weather).country
                min_temp = parse_weather(weather).min_temp
                max_temp = parse_weather(weather).max_temp
                current_temp = parse_weather(weather).current_temp
                wind_speed = parse_weather(weather).wind_speed
                humidity = parse_weather(weather).humidity

                sent = True

            else:
                raise Http404

    else:
        form = CityForm()

    return render(request, "my_app/home.html", locals())

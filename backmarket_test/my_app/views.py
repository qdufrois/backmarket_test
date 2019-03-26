# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from my_app.forms import CityForm


def home(request):
    """View rendering the home page"""

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"]
            sent = True
    
    else:
        form = CityForm()
    

    return render(request, "my_app/home.html", locals())

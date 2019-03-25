# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    """View rendering the home page"""
    return render(request, "my_app/home.html", locals())

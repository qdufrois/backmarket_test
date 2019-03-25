# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.test import TestCase, Client


class TestHome(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        """Testing if the home view is correctly generated"""
        response = self.client.get(reverse("my_app:home"))
        self.assertTrue("<h1>Hello World!</h1>" in str(response.content))

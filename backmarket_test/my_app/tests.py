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
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<h1>Welcome on the back market weather app</h1>" in str(response.content))
    
    def test_form(self):
        response = self.client.post(reverse('my_app:home'), data={'city':'paris'})


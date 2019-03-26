# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.test import TestCase, Client

from forms import CityForm


class TestHome(TestCase):
    def setUp(self):
        self.client = Client()
        self.data_city = {"city": "paris"}

    def test_home(self):
        """Testing if the home view is correctly generated"""
        response = self.client.get(reverse("my_app:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my_app/home.html")
        self.assertTrue(
            "<h1>Welcome on the back market weather app</h1>" in str(response.content)
        )

    def test_form(self):
        """testing if the form is valid"""
        form = CityForm(data=self.data_city)
        self.assertTrue(form.is_valid())
        

    def test_post(self):
        """Testing if the view displays well the expected informations if a valid 
        city was passed in the form post"""         
        response = self.client.post(reverse("my_app:home"), self.data_city)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "<p> Please find the weather of Paris in France </p>"
            in str(response.content).decode("utf-8")
        )

import requests
import json


class API_Request:
    """Class generating a request object from a city input by a client.
    First the woeid for the api is found by using the searching_city method,
    then the weather infos are retrieved using the get weather method
    """

    def __init__(self, city):

        self.city = city
        self.woeid = self.searching_city()

    def searching_city(self):

        url = "https://www.metaweather.com/api/location/search/?query=" + self.city
        result = requests.get(url)
        content = result.json()
        try:
            woeid = content[0]["woeid"]
            return woeid

        except IndexError:
            woeid = False
            return woeid

    def get_weather(self):

        url = "https://www.metaweather.com/api/location/" + str(self.woeid)

        result = requests.get(url)
        content = result.json()

        return content

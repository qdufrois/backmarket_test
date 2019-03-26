class parse_weather:
    """This class parse the data of a dictionnary representing the weather, 
    passed as a parameter, too get clear informations such as the target city and
    country, the minimum and max temps, the wind speed and the humidity
    """

    def __init__(self, weather):

        self.weather = weather
        self.city = weather["title"]
        self.country = weather["parent"]["title"]

        self.min_temp = round(weather["consolidated_weather"][0]["min_temp"], 1)
        self.max_temp = round(weather["consolidated_weather"][0]["max_temp"], 1)
        self.current_temp = round(weather["consolidated_weather"][0]["the_temp"], 1)
        self.wind_speed = round(weather["consolidated_weather"][0]["wind_speed"], 1)
        self.humidity = weather["consolidated_weather"][0]["humidity"]

    def weather_in_n_days(self, n):

        self.city = self.weather["title"]
        self.country = self.weather["parent"]["title"]

        self.min_temp = round(self.weather["consolidated_weather"][0]["min_temp"], 1)
        self.max_temp = round(self.weather["consolidated_weather"][0]["max_temp"], 1)
        self.current_temp = round(self.weather["consolidated_weather"][0]["the_temp"], 1)
        self.wind_speed = round(self.weather["consolidated_weather"][0]["wind_speed"], 1)
        self.humidity = self.weather["consolidated_weather"][0]["humidity"]

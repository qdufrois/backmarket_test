class parse_weather:
    """This class parse the data of a dictionnary representing the weather, 
    passed as a parameter, too get clear informations such as the target city and
    country, the minimum and max temps, the wind speed and the humidity
    """

    def __init__(self, weather, n=0):

        self.weather = weather
        self.city = weather["title"]
        self.country = weather["parent"]["title"]

        self.min_temp = round(weather["consolidated_weather"][n]["min_temp"], 1)
        self.max_temp = round(weather["consolidated_weather"][n]["max_temp"], 1)
        self.current_temp = round(weather["consolidated_weather"][n]["the_temp"], 1)
        self.wind_speed = round(weather["consolidated_weather"][n]["wind_speed"], 1)
        self.humidity = weather["consolidated_weather"][n]["humidity"]

 

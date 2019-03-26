from django.conf.urls import url

from my_app.views import home


app_name = "my_app"

urlpatterns = [
    url(r"^$", home, name="home"),
]

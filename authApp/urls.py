from django.urls import path
from django.views import *

from authApp.views import home
urlpatterns = [
    path('', view=home , name="home")
]

from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('' , views.cars , name="cars"),
    path('single_car/<int:id>/' , views.cars_detail , name="cars_detail"),
    path('search/' , views.search , name="search"),

] 
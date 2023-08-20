from .views import *
from django.urls import path

urlpatterns = [
    path('',list,name="home"),
    path('update/<id>', update ),
    path('delete/<id>', delete ),
]

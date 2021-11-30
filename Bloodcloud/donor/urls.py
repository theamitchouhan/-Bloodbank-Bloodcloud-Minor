from django.contrib import admin
from django.urls import path
from donor import views


urlpatterns = [
    path("donorlogin", views.index, name='donor_login')
]

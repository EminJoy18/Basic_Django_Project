from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_details, name="employee_details"),
    # this is used for dynamic integer value generation that might be the part of the url
]
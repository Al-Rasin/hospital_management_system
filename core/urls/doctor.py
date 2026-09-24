from django.urls import path

from core import views

urlpatterns = [
    path("", views.doctor_list, name="doctor_list"),
    path("add/", views.doctor_add, name="doctor_add"),
]

from django.urls import path

from core import views

urlpatterns = [
    path("", views.patient_list, name="patient_list"),
    path("add/", views.patient_add, name="patient_add"),
    path("<int:pk>/", views.patient_detail, name="patient_detail"),
]

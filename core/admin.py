from django.contrib import admin

from core.models import Appointment, Doctor, Patient, Prescription


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "gender", "phone"]
    search_fields = ["name", "phone"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "specialization", "phone", "room_number"]
    search_fields = ["name", "specialization"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient", "doctor", "scheduled_for", "status"]
    list_filter = ["status", "doctor"]


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ["appointment", "created_at"]


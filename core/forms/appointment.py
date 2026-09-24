from django import forms

from core.models import Appointment, Prescription


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "doctor", "scheduled_for", "reason"]
        widgets = {
            "patient": forms.Select(attrs={"class": "form-select"}),
            "doctor": forms.Select(attrs={"class": "form-select"}),
            "scheduled_for": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "reason": forms.TextInput(attrs={"class": "form-control"}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["diagnosis", "medicines", "notes"]
        widgets = {
            "diagnosis": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "medicines": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

from django import forms

from core.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "specialization", "phone", "room_number"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "specialization": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "room_number": forms.TextInput(attrs={"class": "form-control"}),
        }

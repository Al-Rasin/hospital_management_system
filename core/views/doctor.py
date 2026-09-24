from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.forms import DoctorForm
from core.models import Doctor


@login_required
def doctor_list(request):
    return render(request, "doctors/list.html", {"doctors": Doctor.objects.all()})


@login_required
def doctor_add(request):
    form = DoctorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        doctor = form.save()
        messages.success(request, f"Dr. {doctor.name} added.")
        return redirect("doctor_list")
    return render(request, "doctors/form.html", {"form": form})

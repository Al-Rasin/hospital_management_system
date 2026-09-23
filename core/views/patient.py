from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from core.forms import PatientForm
from core.models import Patient


@login_required
def patient_list(request):
    query = request.GET.get("q", "")
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(name__icontains=query)
    return render(request, "patients/list.html", {"patients": patients, "query": query})


@login_required
def patient_add(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        patient = form.save()
        messages.success(request, f"Patient {patient.name} registered.")
        return redirect("patient_list")
    return render(request, "patients/form.html", {"form": form})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, "patients/detail.html", {"patient": patient})

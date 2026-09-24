from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from core.forms import AppointmentForm, PrescriptionForm
from core.models import Appointment


@login_required
def appointment_list(request):
    status = request.GET.get("status", "")
    appointments = Appointment.objects.select_related("patient", "doctor")
    if status:
        appointments = appointments.filter(status=status)
    return render(
        request,
        "appointments/list.html",
        {
            "appointments": appointments,
            "status": status,
            "status_choices": Appointment.STATUS_CHOICES,
        },
    )


@login_required
def appointment_book(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        appointment = form.save()
        messages.success(request, "Appointment booked.")
        return redirect("appointment_detail", pk=appointment.pk)
    return render(request, "appointments/form.html", {"form": form})


@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(
        Appointment.objects.select_related("patient", "doctor"), pk=pk
    )
    existing = getattr(appointment, "prescription", None)
    form = PrescriptionForm(request.POST or None, instance=existing)

    if request.method == "POST" and form.is_valid():
        prescription = form.save(commit=False)
        prescription.appointment = appointment
        prescription.save()
        # Writing the prescription is what closes the appointment.
        appointment.status = "done"
        appointment.save()
        messages.success(request, "Prescription saved. Appointment marked done.")
        return redirect("appointment_detail", pk=appointment.pk)

    return render(
        request,
        "appointments/detail.html",
        {"appointment": appointment, "form": form, "prescription": existing},
    )


@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = "cancelled"
    appointment.save()
    messages.warning(request, "Appointment cancelled.")
    return redirect("appointment_list")

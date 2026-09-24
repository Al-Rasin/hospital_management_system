from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from core.models import Appointment, Doctor, Patient


@login_required
def dashboard(request):
    today = timezone.localdate()
    return render(
        request,
        "dashboard.html",
        {
            "patient_count": Patient.objects.count(),
            "doctor_count": Doctor.objects.count(),
            "pending_count": Appointment.objects.filter(status="pending").count(),
            "today_count": Appointment.objects.filter(scheduled_for__date=today).count(),
            "recent": Appointment.objects.select_related("patient", "doctor")[:5],
        },
    )

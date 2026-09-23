from django.db import models


class Appointment(models.Model):
    """A booking that links one patient to one doctor at a point in time."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(
        "core.Patient", on_delete=models.CASCADE, related_name="appointments"
    )
    doctor = models.ForeignKey(
        "core.Doctor", on_delete=models.CASCADE, related_name="appointments"
    )
    scheduled_for = models.DateTimeField()
    reason = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["-scheduled_for"]

    def __str__(self):
        return f"{self.patient.name} with {self.doctor} on {self.scheduled_for:%d %b %Y}"


class Prescription(models.Model):
    """What the doctor wrote after an appointment. One per appointment."""

    appointment = models.OneToOneField(
        Appointment, on_delete=models.CASCADE, related_name="prescription"
    )
    diagnosis = models.TextField()
    medicines = models.TextField(help_text="One medicine per line.")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.appointment.patient.name}"

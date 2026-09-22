from django.db import models


class Doctor(models.Model):
    """A doctor who can be booked for appointments."""

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    room_number = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Dr. {self.name}"

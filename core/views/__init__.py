from .appointment import (
    appointment_book,
    appointment_cancel,
    appointment_detail,
    appointment_list,
)
from .dashboard import dashboard
from .doctor import doctor_add, doctor_list
from .patient import patient_add, patient_detail, patient_list

__all__ = [
    "appointment_book",
    "appointment_cancel",
    "appointment_detail",
    "appointment_list",
    "dashboard",
    "doctor_add",
    "doctor_list",
    "patient_add",
    "patient_detail",
    "patient_list",
]

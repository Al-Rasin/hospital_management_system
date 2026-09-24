# Hospital Management System

Django 6.1 + PostgreSQL 18 + Python 3.14.

Team: Rasin, Masud, Muttaqi.

## What it does

| Area | Pages |
|------|-------|
| Auth | Log in, log out. Every page needs a login. |
| Patients | List (with name search), register, detail with appointment history |
| Doctors | List, add |
| Appointments | List (status filter), book, detail, cancel |
| Prescriptions | Written on the appointment detail page; saving one marks the appointment Done |
| Dashboard | Counts of patients, doctors, pending appointments, today's appointments + 5 recent |
| Admin | Django admin registered for all four models |

## Data model

```
Patient  ----< Appointment >----  Doctor
                    |
                    | one-to-one
                    v
              Prescription
```

- `Appointment.patient` and `Appointment.doctor` are ForeignKeys. `on_delete=CASCADE`
  means: delete a patient and their appointments go too, so no appointment is ever
  left pointing at a patient who does not exist.
- `Prescription.appointment` is a OneToOneField: one visit produces one prescription.

## Run it on the Mac

```bash
cd ~/Development/hospital-management-system
./.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000/ and log in as **admin / admin123**.

## Files

```
hospital/          project settings and root urls
core/
  models/          patient.py  doctor.py  appointment.py
  forms/           one ModelForm per model
  views/           patient.py  doctor.py  appointment.py  dashboard.py
  urls/            one url file per area
  admin.py         admin registration
templates/
  base.html        sidebar shell every page extends
  includes/        form_fields.html, status_badge.html - reused snippets
  patients/ doctors/ appointments/ registration/
static/
  css/style.css    the hospital theme
  vendor/          Bootstrap 5.3 + Bootstrap Icons, stored locally
```

Bootstrap is kept in `static/vendor/` instead of loaded from a CDN, so the pages look
correct even with no internet - which matters when demoing inside the VM.

Models, forms, views and urls are **packages** (folders with `__init__.py`), not single
files. That is deliberate: three people can work at the same time without ever editing
the same file, so git never reports a conflict.

## Database

PostgreSQL database `hospitaldb`, connected over the unix socket, so no password is
stored anywhere. `settings.py` picks the DB user from the logged-in OS user, which is
why the same file works on the Mac (`alrasin`) and inside the VM (`rasin`).

Reset from scratch:

```bash
dropdb hospitaldb && createdb hospitaldb
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py createsuperuser
```

## Demo on the Ubuntu VM

Push the current state from the Mac:

```bash
./deploy-to-vm.sh --with-data
```

Then **inside the Ubuntu desktop**, open a terminal and run:

```bash
cd ~/hospital-management-system
./.venv/bin/python manage.py runserver
```

Browse http://127.0.0.1:8000/ in the VM's own browser.

Start the server from the VM desktop, not over SSH. A server started through SSH is
killed the moment the SSH session closes.

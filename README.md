# Hospital Management System

Django 6.1 + PostgreSQL 18 + Python 3.14.

Team: Rasin, Masud, Muttaqi.

## Features

- Login / logout, every page needs login
- Patients: list, search, register, detail
- Doctors: list, add
- Appointments: list, book, cancel
- Prescriptions: written on appointment detail
- Dashboard with counts and recent appointments
- Django admin for all models

## Run

```bash
git clone https://github.com/Al-Rasin/hospital_management_system.git
cd hospital_management_system
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
createdb hospitaldb
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py createsuperuser
./.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000/ and log in with the superuser you made.

## Database

PostgreSQL database `hospitaldb` over unix socket, so no password anywhere.

Reset:

```bash
dropdb hospitaldb && createdb hospitaldb
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py createsuperuser
```

## Structure

```
hospital_management_system/   settings and root urls
core/                         models, forms, views, urls, admin
templates/                    base.html and page templates
static/                       css and Bootstrap
```

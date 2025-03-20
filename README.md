# Healthcare Backend

## Objective

The goal of this project is to build a backend system for a healthcare application using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**. The system allows users to register, log in, and manage **patients** and **doctors** securely.

## Technologies Used

- **Django** (Backend Framework)
- **Django REST Framework (DRF)** (API Management)
- **PostgreSQL** (Database)
- **JWT Authentication** (Secure User Authentication using `djangorestframework-simplejwt`)

---

## Features & Functionalities

- **User Authentication:** Register and login using JWT.
- **Patient Management:** Add, retrieve, update, and delete patient records.
- **Doctor Management:** Add, retrieve, update, and delete doctor records.
- **Patient-Doctor Mapping:** Assign doctors to patients and manage these mappings.
- **Error Handling & Validation:** Ensures data integrity and proper error messages.

---

## Project Structure
health_backend/
│── health_api/
│   │── migrations/
│   │── init.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── serializers.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│
│── health_backend/
│   │── init.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── manage.py
│── requirements.txt
│── readme.md
│── healthEnv/

## API Endpoints

### 1. Authentication APIs

- `POST /api/auth/register/` - Register a new user (name, email, password)
- `POST /api/auth/login/` - Log in a user and return a JWT token

### 2. Patient Management APIs

- `POST /api/patients/` - Add a new patient (Authenticated users only)
- `GET /api/patients/` - Retrieve all patients created by the authenticated user
- `GET /api/patients/<id>/` - Get details of a specific patient
- `PUT /api/patients/<id>/` - Update patient details
- `DELETE /api/patients/<id>/` - Delete a patient record

### 3. Doctor Management APIs

- `POST /api/doctors/` - Add a new doctor (Authenticated users only)
- `GET /api/doctors/` - Retrieve all doctors
- `GET /api/doctors/<id>/` - Get details of a specific doctor
- `PUT /api/doctors/<id>/` - Update doctor details
- `DELETE /api/doctors/<id>/` - Delete a doctor record

### 4. Patient-Doctor Mapping APIs

- `POST /api/mappings/` - Assign a doctor to a patient
- `GET /api/mappings/` - Retrieve all patient-doctor mappings
- `GET /api/mappings/<patient_id>/` - Get all doctors assigned to a specific patient
- `DELETE /api/mappings/<id>/` - Remove a doctor from a patient

---

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/chiragHimself/healthcare_backE.git
cd healthcare_backE
```

## Set Up Virtual Environment
python -m venv healthEnv
source healthEnv/bin/activate  # On MacOS/Linux
healthEnv\Scripts\activate    # On Windows

## Install dependencies 
###pip install -r requirements.txt

## Apply migrations 
python manage.py migrate
python manage.py createsuperuser  # Create an admin user (Follow prompts)

## start a server 
python manage.py runserver

# Server Information

Server will be running at http://127.0.0.1:8000/

## Testing the APIs

You can test the APIs using Postman or any API testing tool.

Make sure to include JWT tokens for protected routes.

Send requests to http://127.0.0.1:8000/api/


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(Group, related_name="custom_user_groups")  
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions") \

'''Model for patient api'''

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link patient to user
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
    
'''Model for patient api'''   
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=255)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
    
''' mapping class for doctor to patient '''
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings")
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # Ensures no duplicate mappings

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
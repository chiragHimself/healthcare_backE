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
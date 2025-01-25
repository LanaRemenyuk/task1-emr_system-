from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model with additional roles."""

    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return self.username


class Patient(models.Model):
    """Model for storing patient info."""

    date_of_birth = models.DateField()
    diagnoses = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Patient {self.id} - {self.diagnoses}'
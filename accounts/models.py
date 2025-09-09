from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # keep username for compatibility, but we'll prefer email for login
    email = models.EmailField('email address', unique=True)

    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.STUDENT
    )

    # optional nice display
    def __str__(self):
        return f"{self.email} ({self.role})"

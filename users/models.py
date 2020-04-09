from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """This model contains all informations regarding the users"""

    birth_date = models.DateField(null=True, blank=True)
    # Add additionnal informations if needed

    def __str__(self):
        return self.username

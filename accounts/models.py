from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=25, blank=True, null=True)
    sap_id = models.IntegerField(blank=True, null=True)
    dept_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=30,default='Student')

    def __str__(self):
        return self.email



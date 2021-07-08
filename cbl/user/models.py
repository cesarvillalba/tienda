from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    tab_number = models.CharField(blank=True, max_length=6)

    def __str__(self):
        return self.user.first_name
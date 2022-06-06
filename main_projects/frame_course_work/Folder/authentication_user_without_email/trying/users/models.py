from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def get_absolute_url(self):
        return reverse('userprofile', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.username

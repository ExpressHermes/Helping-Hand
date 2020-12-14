from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100);

    def save(self, *args, **kwargs):
        self.fullname = self.first_name + ' ' + self.last_name
        super(CustomUser, self).save(*args, **kwargs)
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100, blank=True);

    def save(self, *args, **kwargs):
        if self.fullname.strip() == '':
            self.fullname = self.first_name + ' ' + self.last_name
        if self.fullname.strip() == '':
            self.fullname = self.username
        super(CustomUser, self).save(*args, **kwargs)
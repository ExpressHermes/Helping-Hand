from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    types = [('food','food'), ('clothes','clothes'), ('medical','medical'), ('others','others')]
    type_of_project = models.CharField(max_length=30, default='food', choices = types)
    event_organizer = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    place_name = models.CharField(max_length=350)
    event_type = models.CharField(max_length=50)
    lon = models.DecimalField(max_digits=9,decimal_places=6)
    lat = models.DecimalField(max_digits=9,decimal_places=6)
    description = models.TextField(max_length=500, null=True, blank=True)
    interested = models.ManyToManyField(User, related_name='interested', blank=True)

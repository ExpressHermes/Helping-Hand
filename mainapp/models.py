from django.db import models

class helping_hand(models.Model):
    event_name=models.CharField(max_length=50)
    date=models.DateField()
    place_name=models.CharField(max_length=350)
    longt=models.DecimalField(max_digits=9,decimal_places=6)
    lati=models.DecimalField(max_digits=9,decimal_places=6)
    

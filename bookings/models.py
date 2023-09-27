from datetime import datetime
from django.db import models

# Create your models here.
class Booking(models.Model):
    country=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.first_name
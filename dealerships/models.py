from datetime import datetime
from django.db import models

# Create your models here.
class Dealership(models.Model):
    country=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=100)
    business_experience = models.CharField(max_length=100)
    investment = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.first_name
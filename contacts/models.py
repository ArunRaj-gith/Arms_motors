from datetime import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customer_need = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email
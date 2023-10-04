from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    facebook_link=models.URLField(max_length=100)
    twitter_link=models.URLField(max_length=100)
    instagram_link=models.URLField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    
class New(models.Model):
    photo = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
        

class Certificate(models.Model):
    photo = models.ImageField(upload_to='photos')
    
    
class Showroom_Video(models.Model):
    videofile= models.FileField(upload_to='photos')
    
    
class Bike_Model(models.Model):
    model_name = models.CharField(max_length=100)
    model_image= models.ImageField(upload_to='photos')
    model_range= models.CharField(max_length=100)
    charging_time=models.CharField(max_length=100)
    model_power=models.CharField(max_length=100)
    model_torque=models.CharField(max_length=100)
    model_weight=models.CharField(max_length=100)
    
    def __str__(self):
        return self.model_name
    
    
class Showroom(models.Model):
    photo = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=1000)
    
    
class Award(models.Model):
    photo = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=1000)
    
class Inauguration(models.Model):
    photo = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=1000)
    
class Event(models.Model):
    photo = models.ImageField(upload_to='photos')
    description = models.TextField(max_length=1000)
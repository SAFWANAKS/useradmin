from django.db import models

class userdetails(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    
class contactdetails(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    

    

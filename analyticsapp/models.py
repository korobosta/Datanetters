from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):  
    full_name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100 )  
    subject = models.CharField(max_length=100 )  
    phone=models.CharField(max_length=15)
    message=models.TextField(max_length=255)
    class Meta:  
        db_table = "contact" 

class DataMining(models.Model):
    data_to_mine = models.FileField(upload_to='media/data_mining/')
    name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)  
    phone=models.CharField(max_length=15)
    description=models.TextField(max_length=255)
    class Meta:  
        db_table = "data_mining" 

class DataVisualization(models.Model):
    data_to_visualize = models.FileField(upload_to='media/data_visualization/')
    name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)  
    phone=models.CharField(max_length=15)
    description=models.TextField(max_length=255)
    class Meta:  
        db_table = "data_visualization" 
    
class Dbs(models.Model):
    db_name=models.CharField(max_length=100)
    date_created=models.DateField( null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:  
        db_table = "dbs" 
    
class DataFileStorage(models.Model):
    file_name = models.FileField(upload_to='media/data_file_storage/')
    date_created=models.DateField( null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:  
        db_table = "data_file_storage"

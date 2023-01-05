from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from phone_field import PhoneField
from django.contrib.postgres.fields import ArrayField

@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)
            
def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)

# Create your models here.
class Contact(models.Model):  
    full_name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100 )  
    subject = models.CharField(max_length=100 )  
    phone=models.CharField(max_length=15)
    message=models.TextField(max_length=255)
    date=models.DateField(auto_now=True)
    class Meta:  
        db_table = "contact" 

class DataMining(models.Model):
    data_to_mine = models.FileField(upload_to='media/data_mining/')
    name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)  
    phone=models.CharField(max_length=15)
    description=models.TextField(max_length=255)
    date=models.DateField(auto_now=True)

    class Meta:  
        db_table = "data_mining"
        

class DataVisualization(models.Model):
    data_to_visualize = models.FileField(upload_to='media/data_visualization/')
    name= models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)  
    phone=models.CharField(max_length=15)
    description=models.TextField(max_length=255)
    date=models.DateField(auto_now=True)
    class Meta:  
        db_table = "data_visualization" 
    
class Dbs(models.Model):
    db_name=models.CharField(max_length=100)
    date_created=models.DateField( null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:  
        db_table = "dbs" 
        
class DbTables(models.Model):
    table_name=models.CharField(max_length=100)
    date_created=models.DateField( null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Dbs = models.ForeignKey(Dbs, on_delete=models.CASCADE)
    table_fields=ArrayField(models.CharField(max_length=200))
    class Meta:
        db_table = "db_tables"
    
class DataFileStorage(models.Model):
    file_name = models.FileField(upload_to='media/data_file_storage/')
    date_created=models.DateField( null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:  
        db_table = "data_file_storage"
        
class UserDetails(models.Model):
    image = models.ImageField(upload_to='media/user_images/')
    date_updated=models.DateField( null=False, blank=False, auto_now=True)
    phone = PhoneField( help_text='Contact phone number')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:  
        db_table = "user_details"
    
        

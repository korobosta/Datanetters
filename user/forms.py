from django import forms
from django.contrib .auth.forms import UserCreationForm
from django.contrib.auth.models import User
from analyticsapp.models import Dbs,DataFileStorage,UserDetails,DbTables

class UpdateProfile(forms.ModelForm):
	first_name=forms.CharField(max_length=30, required=True)
	last_name=forms.CharField(max_length=30, required=True)
	email=forms.EmailField(max_length=254,required=True)

	class Meta:
		model=User
		fields=('first_name','last_name','email','username')
		widgets = {
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddDatabaseForm(forms.ModelForm):
	class Meta:
		model = Dbs 
		fields= "__all__" 
		widgets = {
          'db_name': forms.TextInput(attrs={'class': 'form-control'}),
		    
		}
		
class UserDetailsForm(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields= "__all__" 

class TablesForm(forms.ModelForm):
	class Meta:
		model = DbTables
		fields= "__all__" 
        
        
class DataFileStorageForm(forms.ModelForm):
	class Meta:
		model = DataFileStorage
		fields= "__all__" 
		
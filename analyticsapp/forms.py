from django import forms
from django.contrib .auth.forms import UserCreationForm
from django.contrib.auth.models import User
from analyticsapp.models import DataMining, DataVisualization
from django.forms import Textarea

class SignUpForm(UserCreationForm):
	first_name=forms.CharField(max_length=30, required=True, help_text='Enter your first name.')
	last_name=forms.CharField(max_length=30, required=True, help_text='Enter your last name.')
	email=forms.EmailField(max_length=254, required=True, help_text='Enter a valid Email')

	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')
		
		widgets = {
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'username': forms.TextInput(attrs={'class': 'form-control'}),
          'password1': forms.TextInput(attrs={'class': 'form-control'}),
          'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DataMiningForm(forms.ModelForm):
	class Meta:
	    model = DataMining
	    fields= "__all__"
	    widgets = {
          'description': Textarea(attrs={'rows':2, 'cols':25,'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'phone': forms.TextInput(attrs={'class': 'form-control',}),
          'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DataVisualizationForm(forms.ModelForm):
  class Meta:
    model = DataVisualization
    fields= "__all__" 
    widgets = {
          'description': Textarea(attrs={'rows':2, 'cols':25,'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'phone': forms.TextInput(attrs={'class': 'form-control'}),
          'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

  
  
from django import forms
from django.contrib .auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateProfile(UserCreationForm):
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
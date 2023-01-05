from django import forms
from django.forms import Textarea
from analyticsapp.models import Contact  
  
class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = "__all__" 
        widgets = {
          'message': Textarea(attrs={'rows':2, 'cols':25,'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'phone': forms.TextInput(attrs={'class': 'form-control'}),
          'full_name': forms.TextInput(attrs={'class': 'form-control'}),
          'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
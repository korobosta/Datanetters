from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.forms import UpdateProfile
from analyticsapp.ContactForm import ContactForm
from analyticsapp.forms import DataMiningForm, DataVisualizationForm

@login_required 
def home(request):
	username=request.user
	u=User.objects.get(username=username)
	return render(request,'home.html', {'u':u})
def profile(request):
	if request.method == 'POST':
		form = UpdateProfile(data=request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')

			form = UpdateProfile()
		return render(request, 'profile.html', {'form': form})
	else:
		
		
		form = UpdateProfile(instance=request.user) 
		
		return render(request, 'profile.html', {'form': form})
@login_required 
def data_mining(request):
	if request.method == 'POST':
		form = DataMiningForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			
			return redirect('data_mining')

			form = DataMiningForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_mining.html', {'form': form})
	else:
		name=request.user.first_name +" "+ request.user.last_name
		form = DataMiningForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_mining.html', {'form': form})

def machine_learning(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('machine_learning')

			form = ContactForm(initial={'full_name': name,'email':request.user.email})
		return render(request, 'machine_learning.html', {'form': form})
	else:
		name=request.user.first_name +" "+ request.user.last_name
		form = ContactForm(initial={'full_name': name,'email':request.user.email,'subject':'Machine Learning'})
		return render(request, 'machine_learning.html', {'form': form})

def data_visualization(request):
	if request.method == 'POST':
		form = DataVisualizationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			
			return redirect('data_visualization')
			name=request.user.first_name +" "+ request.user.last_name
            
			form = DataVisualizationForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_visualization.html', {'form': form})
	else:
		name=request.user.first_name +" "+ request.user.last_name
		form = DataVisualizationForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_visualization.html', {'form': form})

def database_storage(request):
	template=loader.get_template("./data/database_storage.html")
	return HttpResponse(template.render())

def data_file_storage(request):
	template=loader.get_template("./data/data_file_storage.html")
	return HttpResponse(template.render())

def data_download(request):
	template=loader.get_template("./data/data_download.html")
	return HttpResponse(template.render())

def data_generation(request):
	template=loader.get_template("data_generation.html")
	return HttpResponse(template.render())

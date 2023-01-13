from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from analyticsapp.ContactForm import ContactForm
from analyticsapp.forms import SignUpForm, DataMiningForm, DataVisualizationForm


def index(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		template = loader.get_template("index.html")
		return HttpResponse(template.render())

def about(request):
	template=loader.get_template("about.html")
	return HttpResponse(template.render())

def contact(request):
	template=loader.get_template("contact.html")
	return HttpResponse(template.render())

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your messsage, we will get back to you soon')
			return redirect('contact')

			form = ContactForm()
		return render(request, 'contact.html', {'form': form})
	else:
		form = ContactForm()
		return render(request, 'contact.html', {'form': form})

def process_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
  
    else:
        return redirect('login')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')

			form = SignUpForm()
		return render(request, 'registration/signup.html', {'form': form})
	else:
		form = SignUpForm()
		return render(request, 'registration/signup.html', {'form': form})

def machine_learning(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your machine learing request, we will get back to you soon')

			return redirect('/machine-learning')
			
			form = ContactForm()
		return render(request, './data/machine_learning.html', {'form': form})
	else:
		form = ContactForm()
		return render(request, './data/machine_learning.html', {'form': form})

def data_acquisition(request):
	form = ContactForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your machine learing request, we will get back to you soon')
			return redirect('/machine-learning')
	return render(request, './data/data_acquisition.html', {'form': form})

def data_mining(request):
	if request.method == 'POST':
		form = DataMiningForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your data mining request, we will get back to you soon')
			
			return redirect('/data-mining')

			form = DataMiningForm()
		return render(request, './data/data_mining.html', {'form': form})
	else:
		form = DataMiningForm()
		return render(request, './data/data_mining.html', {'form': form})

def data_visualization(request):
	if request.method == 'POST':
		form = DataVisualizationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your data visualization request, we will get back to you soon')
			
			return redirect('/data-visualization')

			form = DataVisualizationForm()
		return render(request, './data/data_visualization.html', {'form': form})
	else:
		form = DataVisualizationForm()
		return render(request, './data/data_visualization.html', {'form': form})

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
	template=loader.get_template("./data/data_generation.html")
	return HttpResponse(template.render())

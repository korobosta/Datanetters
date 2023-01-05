from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from analyticsapp.models import DataMining, Contact,DataFileStorage,DataVisualization,UserDetails,Dbs,DbTables
import array
import requests
import json
from collections import namedtuple


from user.forms import UpdateProfile,AddDatabaseForm,DataFileStorageForm,UserDetailsForm,TablesForm
from analyticsapp.ContactForm import ContactForm
from analyticsapp.forms import DataMiningForm, DataVisualizationForm

@login_required
def profile(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = UpdateProfile(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile Update Made')
			return redirect('profile')

			form = UpdateProfile()
		return render(request, 'profile.html', {'form': form})
	else:
	   
	    form = UpdateProfile(instance=request.user)
	    return render(request, 'profile.html', {'form': form,'details':details})
		
@login_required
def home(request):
    data_mining_count=DataMining.objects.filter(email=request.user.email).count()
    data_storage_count=DataFileStorage.objects.filter(user=request.user).count()
    data_visualization_count=DataVisualization.objects.filter(email=request.user.email).count()
    machine_learning_count=Contact.objects.filter(email=request.user.email,subject='Machine Learning').count()
    if request.method == 'POST':
        form = UserDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Phone/Image updated')
            return redirect('home')
            form=UserDetailsForm()
            
            
        return redirect(request,'home.html',{'form':form})
    else:
        try:
            details=UserDetails.objects.get(user_id=request.user.id)
        except UserDetails.DoesNotExist:
            details=None
        form = UserDetailsForm()
        return render(request, 'home.html', {'form': form,'details':details,'dmc':data_mining_count,'dsc':data_storage_count,'dvc':data_visualization_count,'mlc':machine_learning_count})
		
		
def change_password(request):
    details=getDetails(request.user.id)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form,'details':details
    })
		
@login_required 
def data_mining(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = DataMiningForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your data mining request, we will get back to you soon')
			
			return redirect('data_mining')

			form = DataMiningForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_mining.html', {'form': form})
	else:
	    mine = DataMining.objects.filter(email=request.user.email)
	    phone=details.phone
	    
	    name=request.user.first_name +" "+ request.user.last_name
	    form = DataMiningForm(initial={'name': name,'email':request.user.email,'phone':phone})
	    return render(request, 'data_mining.html', {'form': form,'mine':mine,'details':details})
		
@login_required 
def machine_learning(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your machine learning request, we will get back to you soon')
			return redirect('machine_learning')

			form = ContactForm(initial={'full_name': name,'email':request.user.email})
		return render(request, 'machine_learning.html', {'form': form})
	else:
	    mlearning = Contact.objects.filter(email=request.user.email,subject='Machine Learning')
	    phone=details.phone
	    name=request.user.first_name +" "+ request.user.last_name
	    form = ContactForm(initial={'full_name': name,'email':request.user.email,'subject':'Machine Learning','phone':phone})
	    return render(request, 'machine_learning.html', {'form': form,'mlearning':mlearning,'details':details})
@login_required 
def data_visualization(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = DataVisualizationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have received your data visualization request, we will get back to you soon')
			
			return redirect('data_visualization')
			name=request.user.first_name +" "+ request.user.last_name
            
			form = DataVisualizationForm(initial={'name': name,'email':request.user.email})
		return render(request, 'data_visualization.html', {'form': form})
	else:
	    visual = DataVisualization.objects.filter(email=request.user.email)
	    name=request.user.first_name +" "+ request.user.last_name
	    phone=details.phone
	   
	    form = DataVisualizationForm(initial={'name': name,'email':request.user.email,'phone':phone})
	    return render(request, 'data_visualization.html', {'form': form,'visual':visual,'details':details})
@login_required 
def database_storage(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = AddDatabaseForm(request.POST)
		if form.is_valid():
			form.save()
			
			return redirect('database_storage')
            
			form = AddDatabaseForm()
		return render(request, 'database_storage.html', {'form': form})
	else:
	    databases=visual = Dbs.objects.filter(user_id=request.user.id)
	    form = AddDatabaseForm()
	    return render(request, 'database_storage.html', {'form': form,'details':details,'databases':databases})
	    
@login_required 
def create_table(request, id):
	if not Dbs.objects.filter(id=id,user_id=request.user.id).exists():
	    messages.success(request, 'Unauthorized DB Access!!!')
	    return redirect('database_storage')
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = TablesForm(request.POST)
		if form.is_valid():
			form.save()
			id=str(id)
			
			return redirect('/home/create-table/'+id)
            
			form = TablesForm()
		return render(request, 'tables.html', {'form': form})
	else:
	    tables=DbTables.objects.filter(user_id=request.user.id,Dbs_id=id)
	    form = TablesForm()
	    return render(request, 'tables.html', {'form': form,'details':details,'tables':tables,'id':id})
	    
@login_required
def add_data(request, id, db):
	if not DbTables.objects.filter(id=id,user_id=request.user.id,Dbs_id=db).exists():
	    messages.success(request, 'Unauthorized DB/Table Access!!!')
	    return redirect('database_storage')
	details=getDetails(request.user.id)

	
	
	if DbTables.objects.filter(id=id,user_id=request.user.id,Dbs_id=db).exists():
	    table=DbTables.objects.get(id=id,user_id=request.user.id,Dbs_id=db)
	else:
	    table=None
	
	table_name=str(request.user) + str(db) + str(table.table_name)
	
	url="https://database-storage.datanetters.co.ke/store_table.php?table_name="+table_name
	response = requests.get(url).json()
	return render(request, 'add_data.html', {'details':details,'table':table,'json_data':response,'table_name':table_name})


def data_download(request):
	template=loader.get_template("./data/data_download.html")
	return HttpResponse(template.render())
	
@login_required
def data_generation(request):
    details=getDetails(request.user.id)
    return render(request, 'data_generation.html', {'details':details})
	
@login_required 
def data_file_storage(request):
	details=getDetails(request.user.id)
	if request.method == 'POST':
		form = DataFileStorageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'File saved')
			
			return redirect('data_file_storage')
            
			form = DataFileStorageForm()
		return render(request, 'data_file_storage.html', {'form': form})
	else:
	    files=DataFileStorage.objects.filter(user_id=request.user.id)
	    form = DataFileStorageForm()
	    return render(request, 'data_file_storage.html', {'form': form,'files':files,'details':details})
		
@login_required 
def delete_data_mining_request(request, id):  
    if DataMining.objects.filter(id=id,email=request.user.email).exists():
        deleterecord = DataMining.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'Request deleted')
        return redirect("data_mining")  
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect("data_mining")
        
@login_required 
def delete_machine_learning_request(request, id):  
    if Contact.objects.filter(id=id,email=request.user.email).exists():
        deleterecord = Contact.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'Request deleted')
        return redirect("machine_learning")  
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect("machine_learning")

@login_required 
def delete_data_file_storage(request, id):  
    if DataFileStorage.objects.filter(id=id,user_id=request.user.id).exists():
        deleterecord = DataFileStorage.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'File Deleted')
        return redirect("data_file_storage")  
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect("data_file_storage")
        
@login_required 
def delete_data_visualization_request(request, id):  
    if DataVisualization.objects.filter(id=id,email=request.user.email).exists():
        deleterecord = DataVisualization.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'Request deleted')
        return redirect("data_visualization")  
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect("data_visualization")
        
@login_required 
def delete_database(request, id):  
    if Dbs.objects.filter(id=id,user_id=request.user.id).exists():
        deleterecord = Dbs.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'Database deleted')
        return redirect("database_storage")  
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect("database_storage")
        
@login_required 
def delete_table(request, id,db):
    db=str(db)
    if DbTables.objects.filter(id=id,user_id=request.user.id,Dbs_id=db).exists():
        deleterecord = DbTables.objects.get(id=id)  
        deleterecord.delete()
        messages.success(request, 'Table deleted')
        return redirect('/home/create-table/'+db) 
    else:
        messages.success(request, 'Unauthorized Delete!!!')
        return redirect('/home/create-table/'+db)
        
def getDetails(id):
    
    try:
        details=UserDetails.objects.get(user_id=id)
    except UserDetails.DoesNotExist:
        details=None
    return details

from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('process-upload', views.upload_data, name='process_upload'),
]
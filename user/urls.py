from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('data-mining', views.data_mining, name='data_mining'),
    path('data-generation', views.data_generation, name='data_generation'),
    path('data-download', views.data_download, name='data_download'),
    path('database-storage', views.database_storage, name='database_storage'),
    path('data-file-storage', views.data_file_storage, name='data_file_storage'),
    path('data-visualization', views.data_visualization, name='data_visualization'),
    path('machine-learning', views.machine_learning, name='machine_learning'),
]
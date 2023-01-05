from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from user import views

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
    path('delete-data-mining-request/<int:id>', views.delete_data_mining_request),  
    path('delete-machine-learning-request/<int:id>', views.delete_machine_learning_request), 
    path('delete-data-file-storage/<int:id>', views.delete_data_file_storage),
    path('delete-data-visualization-request/<int:id>', views.delete_data_visualization_request),
    path('change-password', views.change_password, name='change_password'),
    path('create-table/<int:id>', views.create_table), 
    path('delete-database/<int:id>', views.delete_database), 
    path('delete-table/<int:id>/<int:db>', views.delete_table), 
    path('add-data/<int:id>/<int:db>', views.add_data),
    
]
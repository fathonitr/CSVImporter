from django.urls import path
from . import views

urlpatterns=[
    path('upload/', views.upload_csv, name='upload_csv'),
    path('', views.employees_list, name='employees_list')
]
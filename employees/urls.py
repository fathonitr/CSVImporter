from django.urls import path
from . import views
from rest_framework import routers
from .views_api import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'api/employees', EmployeeViewSet)

urlpatterns=[
    path('upload/', views.upload_csv, name='upload_csv'),
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
] + router.urls
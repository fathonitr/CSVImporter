import csv
from io import TextIOWrapper
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadCSVForm
from .models import Employee
# Create your views here.
def upload_csv(request):
    if request.method =='POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            reader = csv.DictReader(csv_file)

            for row in reader:
                Employee.objects.create(
                    name=row['name'],
                    role=row['role'],
                    salary=row['salary']
                )

            return render(request, 'employees/upload_success.html')
    else:
        form = UploadCSVForm()
    
    return render(request, 'employees/upload.html', {'form': form})

def employee_list(request):
    employees=Employee.objects.all()
    return render(request, "employees/employee_list.html", {"employees": employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        salary = request.POST['salary']
        Employee.objects.create(name=name, role=role, salary=salary)
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html')

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.role = request.POST['role']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_detail', pk=pk)
    return render(request, 'employees/employee_form.html', {'employee': employee})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')

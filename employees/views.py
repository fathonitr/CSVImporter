import csv
from io import TextIOWrapper
from django.shortcuts import render
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

def employees_list(request):
    employees=Employee.objects.all()
    return render(request, "employees/employees_list.html", {"employees": employees})

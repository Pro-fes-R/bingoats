from django.shortcuts import render, redirect
from bingApp.models import Employee
from bingApp.forms import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def getEmployees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html',{'employees':employees})

@login_required
def createEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/list')
    return render(request, 'createEmployee.html', {'form': form})

@login_required
def DeleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/list')

@login_required
def updateEmployee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect ('/list')
    return render(request, 'createEmployee.html', {'form': form})
# we write the home function that needs to be called
# note the syntax, very carefully
from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
    employees = Employee.objects.all()
    
    #print(employees) # will be printed as QuerySet in the terminal
    #all the information of employees
    
    # to rather print this in html, make 'context' dictionary
    context = {
        'employees' : employees,
    }

    return render(request, 'home.html', context)
    #Also change the templates setting in settings.py file
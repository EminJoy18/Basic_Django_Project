from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee

# Create your views here.
def employee_details(request, pk):
    # try:
    #     employee = Employee.objects.get(pk = pk)
    #     print(employee)
    # except:
    #      raise Http404

    # shortcut for the above code
    employee = get_object_or_404(Employee, pk = pk)

    context = {
        'employee' : employee,
    }

    return render(request, 'employee_details.html', context)
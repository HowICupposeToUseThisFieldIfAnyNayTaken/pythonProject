from django.shortcuts import render
from .models import c_employee
def datab_view(request):
    employee_name = c_employee.objects.order_by('full_name')
    employee_work = c_employee.objects.order_by('position')
    employee_date = c_employee.objects.order_by('hired')
    employee_salary = c_employee.objects.order_by('salary')


    return render(request,'datab_app/datab_view.html' , {'employee_t' :employee_name})
# Create your views here.
def datab_sort(request):
    sort_field = 1

    if request.POST.get('sort_name'):
        sort_field = 1
    if request.POST.get('sort_rang'):
        sort_field = 2
    if request.POST.get('sort_salary'):
        sort_field = 3
    if request.POST.get('sort_date'):
        sort_field = 4


    if(sort_field == 1):
        employee = c_employee.objects.order_by('full_name')
    elif (sort_field == 2):
        employee = c_employee.objects.order_by('position')
    elif (sort_field == 4):
        employee = c_employee.objects.order_by('hired')
    elif (sort_field == 3):
        employee = c_employee.objects.order_by('salary')
    else:
        employee = c_employee.objects.order_by('full_name')


    return render(request,'datab_app/datab_sort.html' , {'employee_t' :employee})
# Create your views here.

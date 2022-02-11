from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy

from project2.employees.models import Department, Employee


def home(request):
    # # в setings.py -> MIDDLEWARE зацоментирам 'django.middleware.csrf.CsrfViewMiddleware'
    ## curl --verbose -X POST 'http://127.0.0.1:8000/?sort=name&order=desc'
    # return HttpResponse(f'{request.method}: Tis is home')# през curl да се гледа заявките
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('department details', kwargs={'id': 1, }))
    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(5)],
    }
    return render(request, 'index.html', context)


def department_details(request, id):
    return HttpResponse(f'Tis is department {id}, {type(id)}')


def list_departments(request):# заявки към базата

    # department = Department(name=f'Department {random.randint(1, 1024)}')# това ми създава нов обект
    # department.save()
    # department.pk = random.randint(1024, 2048)# това няма да промени п.кий а ще създаде нов
    # department.save()

    # Department.objects.create(name=f'Department {random.randint(1, 1024)}')# или това , същото е но без save()
    print(Department.objects.get(name='Tv app'))# извежда резултата в конзолата , това връща един резултат
    print(Department.objects.filter(name='Tv app'))# това връща списък , ако не намери резултат, връща празен списък
    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def go_to_home(request):# при грешен url i DEBUG = False в setings.py , 404.html извежда страницата за грешка
    # return redirect(to='/')
    # return redirect('index')
    return redirect('department details', id=random.randint(1024, 2048))


def go_to_dep_details(request):  # 127.0.0.1:8000/department/go/ -> 127.0.0.1:8000/department/random/
    return redirect('department details', id=random.randint(1024, 2048))


def not_found(request):# http://127.0.0.1:8000/department/found/
    return HttpResponseNotFound()
    # raise Http404()

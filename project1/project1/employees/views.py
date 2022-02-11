import random

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


# Create your views here.

# def home(request):# curl --verbose -X GET 'http://127.0.0.1:8000/?sort=name&order=desc'
#     if request.method == 'POST':
#         return HttpResponse(
#             f'{request.method}: This is home',
#             status=201,
#             content_type='text/plain',
#             headers={'x-anton': 'Django'},
#         )
#     else:
#         return HttpResponse('This is Home')
from django.urls import reverse_lazy

from project1.employees.models import Department, Employee


def home(request):
    print(reverse_lazy('list departments'))
    print(reverse_lazy('index'))# визуализира пътя в цонзолата за сверка при работа
    print(reverse_lazy('home'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('dep1'))
    print(reverse_lazy('depid', kwargs={'id': 7}))
    print(reverse_lazy('not found'))

    random_number = random.randint(0, 1024)

    context = {
        'number': random_number,
        'numbers': [random.randint(0, 1024) for _ in range(6)],
    }
    return render(request, 'index.html', context)


def go_to_home(request):# ще редирецтне от 127.0.0.1:8000/go_to_home/ на 127.0.0.1:8000/department/proizwolno/
    # return HttpResponseRedirect()
    return redirect('depid', id=random.randint(0, 1024),)

def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()


def department_details(request):
    return HttpResponse('Tis is Department')


# приема id във view -to и го добавя в пътя
def department_details_2(request, id):
    return HttpResponse(f'Tis is Department {id}, {type(id)}')

# заявки към базата
def list_departments(request):
    # return HttpResponse('This is list of departments')
    department = Department(name=f'Department {random.randint(1, 1024)}'),# създава нов обект
    department.save()# запазва го в базата

    department.pk = random.randint(1024, 2048)# смяната на pk не сменя ключа а създава нов
    department.save()

    print(Department.objects.filter(name='Tv app')) # връща списък , може и да е празен
    print(Department.objects.get(name='Tv app'))#  аз нямам в случая tv app  в моята база, ако не го намери гърми

    Department.objects.create(name=f'Department {random.randint(1, 1024)}')# това го създава и го добавя автоматично

    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        # 'departments': Department.objects.filter(name__iendswith='app'),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create_department(request):
    return HttpResponse('Created')

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


def home(request):
    print(reverse_lazy('index'))# визуализира пътя в цонзолата за сверка при работа
    print(reverse_lazy('home'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
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


def list_departments(request):
    return HttpResponse('This is list of departments')

def create_department(request):
    return HttpResponse('Created')

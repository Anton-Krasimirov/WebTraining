from django.shortcuts import render


# Create your views here.
from project1.employees.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.order_by('department__name','first_name', '-last_name').all()]
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'title': 'EmplOYees List',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab commodi dicta eligendi, '
                       'error exercitationem, labore libero magnam nam necessitatibus nihil officiis omnis, '
                       'quam tempore tenetur ullam vel veritatis voluptas? Atque?',
        # 'employees': employees,
        # 'department_names': [d.name for d in Department.objects.all()],
    }
    return render(request, 'templates_examples/index.html', context)# подавам към темплейта

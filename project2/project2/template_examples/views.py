from django.shortcuts import render

from project2.employees.models import Employee, Department


def index(request):
    # employees = [e for e in Employee.objects.order_by('first_name', '-last_name').all()]
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'title': 'emplOyeEs List',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias asperiores cumque cupiditate distinctio dolor',
        'employees': Employee.objects.order_by('department__name', 'first_name', '-last_name').all(),
        'department_names': [d.name for d in Department.objects.all()],
    }

    return render(request, 'Templates_examples/index.html', context)# подавам към Templates_examples/index.html

from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy

from project2.employees.models import Department, Employee

from django import forms

# Собствен валидатор
def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',  # form-control добре е да се прави е html-a
#             }
#         )
#     )
#     last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}, ))
#
#     # required прави полето незадължително за попълване
#     age = forms.IntegerField(
#         required=False,
#         widget=forms.TextInput(attrs={'class': 'form-control', }),  # 'type': 'range',
#         validators=(validate_positive,),
#     )
#
#     egn = forms.CharField(max_length=10, )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DEVOPS Engineer'),
#         )
#     )
#
#     companies = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES),
#     )


# Модел форми синтаксис
class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(widget=forms.HiddenInput(), required=False, )# създава скрито поле за защита от ботове
    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name', 'egn')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'})
        }

# целта е да не може да се променя egn , това е рестрикцията, ипроменяме на EditEmployeeForm във def edit_employee
class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(attrs={'readonly': 'readonly'},)
        }



# Форма за сортиране
class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        ),
    )



def home(request):  # визуализираме формата
    return render(request, 'index.html', )


def create_employee(request):  # обработваме формата
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)  # взимаме входните данни за обработка
        if employee_form.is_valid():
 # save to database
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     egn=employee_form.cleaned_data['egn'],
            #     companies=employee_form.cleaned_data['companies'],
            #     department_id=1,
            # )
# също като горното но оптимизирано
#             emp = Employee(
#                 **employee_form.cleaned_data,
#                 department_id=1,
#             )
#             emp.full_clean()  # валидаторите вав обикновенна форма трябва де се извикат експлицитно
#             emp.save()
            employee_form.save()
            return redirect('index')

    else:
        employee_form = EmployeeForm()
# тук ползваме формата за сортиране с гет
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')# това order_by го взимаме от формата за сортиране

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,

    }
    return render(request, 'create.html', context)


# def create_employee(request):  # обработваме формата
#     # print(request.method)
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#         return render(request, 'create.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)  # взимаме входните данни за обработка
#         if employee_form.is_valid():
#             return redirect('index')
#         context = {
#             'employee_form': employee_form,
#         }
#         return render(request, 'create.html', context)


# def home(request):
# # # в setings.py -> MIDDLEWARE зацоментирам 'django.middleware.csrf.CsrfViewMiddleware'
# ## curl --verbose -X POST 'http://127.0.0.1:8000/?sort=name&order=desc'
# # return HttpResponse(f'{request.method}: Tis is home')# през curl да се гледа заявките
# print(reverse_lazy('index'))
# print(reverse_lazy('go to home'))
# print(reverse_lazy('list departments'))
# print(reverse_lazy('department details', kwargs={'id': 1, }))
# context = {
# 'number': random.randint(0, 1024),
# 'numbers': [random.randint(0, 1024) for _ in range(5)],
# }
# return render(request, 'index.html', context)


# def department_details(request, id):
#     return HttpResponse(f'Tis is department {id}, {type(id)}')
#
#
# def list_departments(request):# заявки към базата
#
#     # department = Department(name=f'Department {random.randint(1, 1024)}')# това ми създава нов обект
#     # department.save()
#     # department.pk = random.randint(1024, 2048)# това няма да промени п.кий а ще създаде нов
#     # department.save()
#
#     # Department.objects.create(name=f'Department {random.randint(1, 1024)}')# или това , същото е но без save()
#     print(Department.objects.get(name='Tv app'))# извежда резултата в конзолата , това връща един резултат
#     print(Department.objects.filter(name='Tv app'))# това връща списък , ако не намери резултат, връща празен списък
#     context = {
#         'departments': Department.objects.prefetch_related('employee_set').all(),
#         'employees': Employee.objects.all(),
#     }
#     return render(request, 'list_departments.html', context)
#
#
# def go_to_home(request):# при грешен url i DEBUG = False в setings.py , 404.html извежда страницата за грешка
#     # return redirect(to='/')
#     # return redirect('index')
#     return redirect('department details', id=random.randint(1024, 2048))
#
#
# def go_to_dep_details(request):  # 127.0.0.1:8000/department/go/ -> 127.0.0.1:8000/department/random/
#     return redirect('department details', id=random.randint(1024, 2048))
#
#
# def not_found(request):# http://127.0.0.1:8000/department/found/
#     return HttpResponseNotFound()
#     # raise Http404()

def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')

    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form
    }

    return  render(request, 'edit.html', context)
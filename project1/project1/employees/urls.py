from django.urls import path

from project1.employees.views import home, department_details, list_departments, department_details_2, not_found, \
    create_department

urlpatterns = [
    path('list/', list_departments, name='list departments'),
    path('create/', create_department),
    path('<id>/', department_details_2, name='depid'),

    path('', home, name='home'),
    path('1/', department_details, name='dep1'),

    path('not_found', not_found, name='not found'),
]
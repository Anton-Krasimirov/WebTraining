from django.urls import path

from project2.employees.views import department_details, list_departments, go_to_dep_details, not_found

urlpatterns = [
    # path('<int:id>/', department_details),
    path('go/', go_to_dep_details),# 127.0.0.1:8000/department/go/
    path('found/', not_found),
    path('<id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),


]

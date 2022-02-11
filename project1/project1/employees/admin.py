from django.contrib import admin

# Register your models here.
from project1.employees.models import Employee, Department


# синтаксис за създаване на администрация 172.0.0.1:8000/admin/
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title', 'company',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
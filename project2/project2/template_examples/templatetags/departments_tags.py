from django import template

from project2.employees.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')# в скобите поставяме фаила който искаме да зарежда
def departments_list():
    departments = Department.objects.prefetch_related('employee_set').all()

    # departments[0].employee_set.count()

    # context
    return {
        'departments': departments
    }

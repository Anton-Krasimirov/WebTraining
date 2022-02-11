from django import template

from project1.employees.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')
def departments_list():
    departments = Department.objects.prefetch_related('employee_set').all()
    return {'departments': departments,}

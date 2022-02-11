from django.urls import path

from project1.template_examples.views import index

urlpatterns = (
    path('', index, name='templates index'),
)
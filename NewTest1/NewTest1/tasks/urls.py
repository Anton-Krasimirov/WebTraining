from django.urls import path

from NewTest1.tasks.views import home

# App
urlpatterns = (
    path('', home),  # localhost:8001/
)

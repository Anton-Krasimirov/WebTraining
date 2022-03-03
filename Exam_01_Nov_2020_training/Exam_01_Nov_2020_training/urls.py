
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Exam_01_Nov_2020_training.Recipes.urls')),
]

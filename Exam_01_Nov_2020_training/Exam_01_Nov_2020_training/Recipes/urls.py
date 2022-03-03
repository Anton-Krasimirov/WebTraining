from django.urls import path

from Exam_01_Nov_2020_training.Recipes.views import home_page, create, edit, delete, details

urlpatterns = [
    path('', home_page, name='home page'),# home page
    path('create/', create, name='create'), # create recipe page
    path('edit/<int:id>/', edit, name='edit'), # edit recipe page
    path('delete/<int:id>/', delete, name='delete'), # delete recipe page
    path('details/<int:id>/', details, name='details'), # recipe details page

]
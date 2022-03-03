from django.urls import path

from Exam_27_06_training.Notes.views import add_note, edit_note, delete_note, note_details, home_page, profile, \
        create_profile

urlpatterns = [
        path('', home_page, name='home'), # home page
        path('profile/create/', create_profile, name='create profile'),
        path('add/', add_note, name='add note'), # add note page
        path('edit/<int:pk>/', edit_note, name='edit note'), # edit note page
        path('delete/<int:pk>/', delete_note, name='delete note'), # delete note page
        path('details/<int:pk>/', note_details, name='note details'), # note details page
        path('profile/', profile, name='profile'), # profile page

]
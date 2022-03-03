from django.urls import path

from Exam110821_training.OnlineLibrary.views import home_page, book_add, book_edit, book_details, profile, profile_edit, \
    profile_delete, create_profile

urlpatterns = [
    path('', home_page, name='home'),
    path('add/', book_add, name='book add'),
    path('edit/<int:id>', book_edit, name='book edit'),
    path('details/<int:id>', book_details, name='book details'),
    path('create/', create_profile, name='create profile'),
    path('profile/', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile edit'),
    path('profile/delete', profile_delete, name='profile delete'),
]
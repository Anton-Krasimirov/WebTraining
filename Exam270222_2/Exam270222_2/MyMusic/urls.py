from django.urls import path

from Exam270222_2.MyMusic.views import home_page, add_album, details_album, edit_album, delete_album, create_profile, \
    profile_details, profile_delete

urlpatterns = [
    path('', home_page, name='home page'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),

    path('album/add/', add_album, name='album add'),
    path('album/details/<int:id>/', details_album, name='album details'),
    path('album/edit/<int:id>/', edit_album, name='album edit'),
    path('album/delete/<int:id>/', delete_album, name='album delete'),
]
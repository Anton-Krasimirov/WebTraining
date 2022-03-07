from django.shortcuts import render

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items': True,#  за да не ни се показват допълнителните полета, проверката е в темплейта
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()

    # filter казва: вземими от таблица pets всички pet  чийто user_profile е == на profile
    # prefetch_related  е да работи базата по бързо с по малко заявки, казва вземи свързаните
    pet_photos = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .filter(tagged_pets__user_profile=profile) \
        .distinct()

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)

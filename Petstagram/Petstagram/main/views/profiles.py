from django.shortcuts import render, redirect

from petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main.models import PetPhoto, Pet, Profile
from petstagram.main.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))

    pet_photos = PetPhoto.objects \
        .filter(tagged_pets__in=pets) \
        .distinct()# distinct() дава само уникалните

    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
        'pets': pets,
    }

    return render(request, 'profile_details.html', context)

# тази функция я викам на всеки return  по-долу, другия вариянт е закоментиран отдолу
def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
    }

    return render(request, template_name, context)

''' Profile() прави празен профил за да го предадем на form във profile_action, за да може кодато се рендерира template_name
да се покаже страницата с празни полета, попълвайки ги се връща на същото вю , самоче с пост и качвайкисе пак вав
 функцията в request.POST има вече стйности от полетат които са попълнени '''
def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')

#
# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profile_edit.html', context)

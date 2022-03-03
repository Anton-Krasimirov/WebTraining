from django.shortcuts import render, redirect

from Exam270222_2.MyMusic.forms import CreateProfile, CreateAlbum
from Exam270222_2.MyMusic.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


'''ако е GET отива в else , има нова форма и я визуализира, ако е POST проверява дали е валидна , ако е отива в home page
ako e POST  и е невалидна , ние сме я направили във  form , няма да се изпълни  return , а ще отиде на context и след това на 
return render'''
def create_profile(request):  # на 1.31.30 ч. от лекция Forms  е разяснение стъпките на така дефинираното view
    if request.method == 'POST':
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfile()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbum(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateAlbum()

    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def details_album(request, id):
    album = Album.objects.get(id=id)
    image = Album.objects.get(id=id).image_URL
    artist = Album.objects.get(id=id).album_name
    genre = Album.objects.get(id=id).genre
    price = Album.objects.get(id=id).price
    description = Album.objects.get(id=id).description

    context = {
        'album': album,
        'image': image,
        'artist': artist,
        'genre': genre,
        'price': price,
        'description': description
    }

    return render(request, 'album-details.html', context)


def edit_album(request, id):
    pass


def delete_album(request, id):
    pass


def profile_details(request):
    pass


def profile_delete(request):
    pass

# Create your views here.

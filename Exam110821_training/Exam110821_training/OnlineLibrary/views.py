from django.shortcuts import render, redirect

from Exam110821_training.OnlineLibrary.forms import CreateProfileForm, AddBookForm
from Exam110821_training.OnlineLibrary.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None



def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()
    form = CreateProfileForm()


    context = {
        'form': form,
        'books': books,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,# за да може Profile  да не се показва когато няма още наличен профил
    }
    return render(request, 'home-no-profile.html', context)



def book_add(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm()

    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def book_edit(request, id):
    pass


def book_details(request, id):
    pass


def profile(request):
    pass


def profile_edit(request):
    pass


def profile_delete(request):
    pass
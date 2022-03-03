

from django.shortcuts import render, redirect

# Create your views here.
from Exam_27_06_training.Notes.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from Exam_27_06_training.Notes.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()
    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)# request.FILES слагаме когато работим с images в случая не работим
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,  # за да може Profile  да не се показва когато няма още наличен профил
    }
    return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):# TODO # триенето на профил е добре да се прави в Forms , виж ExamPreparetion1
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    title = Note.objects.get(pk=pk).title
    content = Note.objects.get(pk=pk).content
    image = Note.objects.get(pk=pk).image_url

    context = {
        'title': title,
        'content': content,
        'image': image,
        'note': note,
    }

    return render(request, 'note-details.html', context)


def profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    count = len(notes)
    context = {
        'profile': profile,
        'notes': notes,
        'count': count,
    }
    return render(request, 'profile.html', context)

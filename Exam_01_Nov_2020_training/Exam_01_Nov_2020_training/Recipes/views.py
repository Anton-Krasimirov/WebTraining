from django.shortcuts import render, redirect
import re
# Create your views here.
from Exam_01_Nov_2020_training.Recipes.forms import CreateRecipe, DetailsRecipe, EditRecipe, DeleteRecipe
from Exam_01_Nov_2020_training.Recipes.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipe()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        form = EditRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditRecipe(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = DeleteRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteRecipe(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)

def details(request, id):

    recipe = Recipe.objects.get(id=id)
    # form = DetailsRecipe(instance=recipe)
    text = recipe.ingredients
    ingredients = text.split(", ")
    context = {
        'recipe': recipe,
        # 'form': form,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)
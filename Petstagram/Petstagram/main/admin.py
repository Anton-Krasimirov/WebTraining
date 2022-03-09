from django.contrib import admin

from petstagram.main.models import Profile, Pet, PetPhoto

# за да създаде в администрацията формички за създаване , добавяме ги в ProfileAdmin като inlines
class PetInlineAdmin(admin.StackedInline):
    model = Pet

# така регистрираме модел в регистрацията да ни се покаже#
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')# за по красиво показване в администрацията


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass

from django import forms

from ExamPreparation1.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'image', )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'image', )
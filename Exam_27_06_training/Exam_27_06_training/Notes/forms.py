import os

from django import forms

from Exam_27_06_training.Notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'age', 'image_url',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            # field.widget.attrs['readonly'] = 'readonly'# това прави полетата само четими
            field.widget.attrs['disabled'] = 'disabled'  # това прави полетата не активни , потъмнени
            field.required = False

    # def save(self, commit=True):  # изтриването е добре да става вав формата
    #     image_path = self.instance.image_url.path  # взима пътя на снимката
    #     if commit:
    #         self.instance.delete()  # изтрива инстанцията на профила която е зададена
    #         Note.objects.all().delete()  # трие всички expenses  на профила
    #         os.remove(image_path)  # това трие смимката на профила от файловата система , който ще остане
    #     return self.instance
    #
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image',
        }



import os

from django import forms

from ExamPreparation1.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'image', )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'budget': 'Budget',
            'image': 'Profile Image',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'image', )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'budget': 'Budget',
            'image': 'Profile Image',
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):# изтриването е добре да става вав формата
        image_path = self.instance.image.path# взима пътя на снимката
        if commit:
            self.instance.delete()# изтрива инстанцията на профила която е зададена
            Expense.objects.all().delete()# трие всички expenses  на профила
            os.remove(image_path)  # това трие смимката на профила от файловата система , който ще остане
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }



class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):# тази функция прави полетата във формата да се четат само, да не могат да се пишат
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'
            # field.required = False


    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }

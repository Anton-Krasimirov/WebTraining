from django import forms
import os

from Exam270222_2.MyMusic.models import Profile, Album


class CreateProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):# за да вземе от инита всичко , без да знам какво и как идва ПРЕДПОЛАГАМ
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age',)
# widgets ни валидира до някаква степен инпут полетата на формите , и прави наша визуализация , различна от дефолтната
# placeholder например задава какво да бъде изписано вътре в полето за въвеждане
        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text', 'name': 'username', 'id': 'first_name', 'placeholder': 'Username',
            })
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }



class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album

        fields = ('album_name', 'artist', 'genre', 'description', 'image_URL', 'price',)
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_URL': 'Image URL',
            'price': 'Price',
        }


class DetailsAlbum(forms.ModelForm):
    class Meta:
        model = Album
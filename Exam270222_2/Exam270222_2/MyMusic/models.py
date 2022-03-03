from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models



def validate_username(value):

    if not all(v.isalnum() or not v == '_' for v in value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15
    MIN_AGE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_username,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(MIN_AGE),),

    )



class Album(models.Model):
    MIN_FLOAD_VALUE = 0
    Ganre_music = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Rock Music', 'Rock Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(max_length=30)

    genre = models.CharField(
        max_length=30,
        choices=Ganre_music,
        # (
        #     ('Pop Music', 'Pop Music'),
        #     ('Jazz Music', 'Jazz Music'),
        #     ('R&B Music', 'R&B Music'),
        #     ('Rock Music', 'Rock Music'),
        #     ('Rock Music', 'Rock Music'),
        #     ('Dance Music', 'Dance Music'),
        #     ('Hip Hop Music', 'Hip Hop Music'),
        #     ('Other', 'Other'),
        # ),
    )

    description = models.TextField(null=True, blank=True, )

    image_URL = models.URLField()

    price = models.FloatField(
        validators=(MinValueValidator(MIN_FLOAD_VALUE),),
    )
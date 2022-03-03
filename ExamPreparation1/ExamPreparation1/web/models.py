from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def validate_only_leters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


'''когато стойноста за проверка е динамична (не е само една конкретна стойност) се прави с клас чиято инстанция
може да се вика като метод'''


@deconstructible  # задължителен декоратор за валидатор класове, пази с какви стойности е извикан инит и после ги подава същите
class MaxFilesInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):  # това прави инстанцията да се вика като метод
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    BUDGET_DEFAULT = 0
    BUDGET_MIN_VALUE = 0
    IMAGE_IN_MAX_SIZE_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_leters,
        )
    )

    last_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_leters,
        ),
    )

    budget = models.IntegerField(
        default=BUDGET_DEFAULT,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),),
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,  # добре е да се зададе да се ъплоудват на едно място медиа файловете
        null=True,
        blank=True,  # тези две стойности се добавят ако трябва да е optional
        validators=(
            MaxFilesInMbValidator(IMAGE_IN_MAX_SIZE_MB),
        )
    )

    @property# това пропърти дава името на профила в темплейта му
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    title = models.CharField(max_length=30, )

    image = models.URLField()# ако поставим в скобите verbose_name='Link to Image' ще го визуализира по зададения в кавичките

    description = models.TextField(null=True, blank=True, )

    price = models.FloatField()

    class Meta:
        ordering = ('title', 'price',)# сортира expenses да не ги разменя и да не стане грешка при edit

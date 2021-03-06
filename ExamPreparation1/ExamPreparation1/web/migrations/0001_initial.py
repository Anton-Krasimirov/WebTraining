# Generated by Django 4.0.2 on 2022-02-17 13:18

import ExamPreparation1.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), ExamPreparation1.web.models.validate_only_leters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), ExamPreparation1.web.models.validate_only_leters])),
                ('budget', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[ExamPreparation1.web.models.MaxFilesInMbValidator(5)])),
            ],
        ),
    ]

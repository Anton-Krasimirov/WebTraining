# Generated by Django 4.0.2 on 2022-02-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_alter_employee_egn'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
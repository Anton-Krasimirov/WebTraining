# Generated by Django 4.0.2 on 2022-02-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_egn'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id2', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, default='NO NAME', max_length=40, null=True),
        ),
    ]
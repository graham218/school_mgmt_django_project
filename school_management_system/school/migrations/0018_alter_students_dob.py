# Generated by Django 3.2 on 2022-01-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_alter_students_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='DOB',
            field=models.DateTimeField(),
        ),
    ]

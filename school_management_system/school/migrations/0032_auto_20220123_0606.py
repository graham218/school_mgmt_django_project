# Generated by Django 3.2 on 2022-01-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0031_marks_yr1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks_yr1',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='marks_yr1',
            name='last_name',
        ),
    ]
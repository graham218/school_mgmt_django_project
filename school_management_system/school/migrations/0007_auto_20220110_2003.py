# Generated by Django 3.2 on 2022-01-10 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20220110_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='students',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='students',
            name='user',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Stages',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]

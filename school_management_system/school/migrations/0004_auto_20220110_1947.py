# Generated by Django 3.2 on 2022-01-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20211230_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='units',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='units',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='students',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='students_pic'),
        ),
    ]

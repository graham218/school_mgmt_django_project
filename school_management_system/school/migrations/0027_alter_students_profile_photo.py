# Generated by Django 3.2 on 2022-01-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0026_auto_20220114_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='students_pic/'),
        ),
    ]

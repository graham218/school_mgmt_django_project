# Generated by Django 3.2 on 2022-01-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_alter_students_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
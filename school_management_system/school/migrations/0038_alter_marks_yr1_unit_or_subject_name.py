# Generated by Django 3.2 on 2022-01-23 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0037_auto_20220123_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_yr1',
            name='unit_or_subject_name',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units'),
        ),
    ]

# Generated by Django 3.2 on 2022-01-19 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0029_auto_20220119_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectures',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='programme',
            field=models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.programmes'),
        ),
    ]

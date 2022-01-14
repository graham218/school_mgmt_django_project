# Generated by Django 3.2 on 2022-01-14 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_auto_20220114_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='programme',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.programmes'),
        ),
        migrations.AlterField(
            model_name='students',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.stages'),
        ),
    ]
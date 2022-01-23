# Generated by Django 3.2 on 2022-01-23 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0041_auto_20220123_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturerUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_understanding', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.lectures')),
                ('unit_name', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('username', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

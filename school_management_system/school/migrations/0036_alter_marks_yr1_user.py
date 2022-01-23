# Generated by Django 3.2 on 2022-01-23 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0035_alter_marks_yr1_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_yr1',
            name='user',
            field=models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

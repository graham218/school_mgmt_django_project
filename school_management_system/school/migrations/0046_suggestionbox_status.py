# Generated by Django 3.2 on 2022-01-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0045_suggestionbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionbox',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
# Generated by Django 3.2 on 2022-02-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0052_auto_20220208_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

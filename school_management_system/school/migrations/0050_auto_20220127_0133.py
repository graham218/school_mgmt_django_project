# Generated by Django 3.2 on 2022-01-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0049_auto_20220127_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noticeboard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
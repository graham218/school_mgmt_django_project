# Generated by Django 3.2 on 2022-01-23 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0040_fee_payment_feereceipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='feereceipt',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='SpecialExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_name', models.CharField(blank=True, max_length=255, null=True)),
                ('marks', models.CharField(blank=True, max_length=255, null=True)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('date_paid', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

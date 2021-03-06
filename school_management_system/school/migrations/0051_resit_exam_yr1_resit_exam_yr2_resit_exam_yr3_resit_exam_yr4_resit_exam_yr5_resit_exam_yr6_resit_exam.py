# Generated by Django 3.2 on 2022-03-05 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0050_noticeboard_notice_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='resit_exam_yr7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resit_exam_yr1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('stage', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.stages')),
                ('unit_name', models.ForeignKey(blank=True, default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.units')),
                ('user', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

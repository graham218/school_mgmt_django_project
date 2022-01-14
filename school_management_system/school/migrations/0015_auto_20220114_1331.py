# Generated by Django 3.2 on 2022-01-14 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_auto_20220114_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_admission',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_graduation',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='programme',
            field=models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='school.programmes'),
        ),
        migrations.AlterField(
            model_name='students',
            name='stage',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.stages'),
        ),
        migrations.AlterField(
            model_name='students',
            name='stud_gender',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.gender'),
        ),
        migrations.AlterField(
            model_name='students',
            name='total_fees_billed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='total_fees_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]

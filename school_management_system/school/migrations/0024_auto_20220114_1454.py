# Generated by Django 3.2 on 2022-01-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0023_alter_students_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='admission_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='birth_cert_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='national_ID_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='nationality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='postal_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='students_pic/'),
        ),
        migrations.AlterField(
            model_name='students',
            name='school_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='school_email_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.stages'),
        ),
        migrations.AlterField(
            model_name='students',
            name='stud_gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.gender'),
        ),
        migrations.AlterField(
            model_name='students',
            name='total_fees_billed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='total_fees_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

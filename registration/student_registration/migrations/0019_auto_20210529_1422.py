# Generated by Django 3.1.7 on 2021-05-29 14:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0018_studentdetails_grade_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetails',
            old_name='active_record',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='enrolment_for_year',
            field=models.IntegerField(choices=[(None, 'Choose Year'), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031)], null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='profile_photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/attachments/', location='/apps/alimregistration/registration/attachments'), upload_to='attachments/'),
        ),
    ]

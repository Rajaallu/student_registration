# Generated by Django 3.1.7 on 2021-05-15 08:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0006_auto_20210515_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='profile_photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/', location=''), upload_to='attachments/'),
        ),
    ]

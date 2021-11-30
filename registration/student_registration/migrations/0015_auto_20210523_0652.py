# Generated by Django 3.1.7 on 2021-05-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_registration', '0014_auto_20210523_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_name',
            field=models.CharField(default='', help_text='Template Name', max_length=100, verbose_name='Template Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='curr_iqra_grade',
            field=models.IntegerField(null=True),
        ),
    ]
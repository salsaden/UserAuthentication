# Generated by Django 3.2.12 on 2023-08-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='intake',
            field=models.CharField(default='January', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='studymode',
            field=models.CharField(default='Regular', max_length=200),
        ),
    ]
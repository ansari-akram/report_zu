# Generated by Django 3.2 on 2022-04-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0005_departmentadminuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentadminuser',
            name='usertype',
            field=models.CharField(max_length=50),
        ),
    ]
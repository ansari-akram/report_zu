# Generated by Django 3.2 on 2022-04-24 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report_app', '0008_auto_20220423_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentadminuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

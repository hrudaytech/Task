# Generated by Django 4.2.3 on 2023-07-06 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employeeAPP", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="manager",
        ),
    ]
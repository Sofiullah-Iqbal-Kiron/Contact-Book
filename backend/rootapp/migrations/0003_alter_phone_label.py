# Generated by Django 4.2.5 on 2023-10-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rootapp", "0002_alter_contact_options_alter_phone_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone",
            name="label",
            field=models.CharField(default="", max_length=60),
        ),
    ]

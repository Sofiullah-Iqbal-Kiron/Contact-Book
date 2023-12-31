# Generated by Django 4.2.5 on 2023-10-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rootapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["first_name"]},
        ),
        migrations.AlterModelOptions(
            name="phone",
            options={"ordering": ["number"]},
        ),
        migrations.AlterField(
            model_name="contact",
            name="about",
            field=models.CharField(
                default="",
                max_length=100,
                verbose_name="company, abstract or short details",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="address",
            field=models.TextField(default="", verbose_name="full address"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="details",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(
                default="no-email-provided@example.com",
                max_length=254,
                verbose_name="personal email",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AlterField(
            model_name="contact",
            name="middle_name",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AlterField(
            model_name="contact",
            name="nick_name",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AlterField(
            model_name="contact",
            name="relation",
            field=models.CharField(
                default="", max_length=100, verbose_name="relation with current user"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="website",
            field=models.URLField(
                default="example.com", verbose_name="personal website, if any"
            ),
        ),
    ]

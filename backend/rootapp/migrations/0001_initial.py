# Generated by Django 4.2.5 on 2023-09-28 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rootapp.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=60)),
                ("middle_name", models.CharField(blank=True, max_length=30, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                ("nick_name", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="personal email",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True, null=True, verbose_name="personal website, if any"
                    ),
                ),
                (
                    "relation",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="relation with current user",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="person picture",
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "address",
                    models.TextField(
                        blank=True, null=True, verbose_name="full address"
                    ),
                ),
                (
                    "about",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="company, abstract or short details",
                    ),
                ),
                ("details", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "of",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "country_code",
                    models.CharField(
                        choices=[("+880", "BD")], default="BD", max_length=4
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        validators=[rootapp.validators.phone_number_validator],
                    ),
                ),
                ("label", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "of",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="numbers",
                        to="rootapp.contact",
                    ),
                ),
            ],
        ),
    ]

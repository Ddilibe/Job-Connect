# Generated by Django 5.1.4 on 2024-12-11 08:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "monthly_salary",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.TextField(blank=True, null=True)),
                ("no_of_opening", models.IntegerField(blank=True, null=True)),
                (
                    "application_starting_date",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "application_ending_date",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("active", models.BooleanField(blank=True, default=True, null=True)),
                (
                    "job_thumbnail",
                    models.FileField(blank=True, null=True, upload_to="photos"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ApplicationForm",
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
                ("full_name", models.TextField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("cover_letter", models.TextField(blank=True, null=True)),
                ("resume", models.FileField(blank=True, null=True, upload_to="photos")),
                (
                    "application_date",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("status", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_root_api_job_api.job",
                    ),
                ),
            ],
        ),
    ]

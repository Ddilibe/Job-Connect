# Generated by Django 5.1.4 on 2024-12-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "core_root_api_job_api",
            "0004_alter_applicationform_application_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="job_requirements",
            field=models.TextField(blank=True, null=True),
        ),
    ]
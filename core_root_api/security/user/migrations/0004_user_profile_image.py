# Generated by Django 5.1.4 on 2024-12-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_root_api_security_user", "0003_companyprofile_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_image",
            field=models.FileField(blank=True, null=True, upload_to="photos"),
        ),
    ]
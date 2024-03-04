# Generated by Django 4.2.10 on 2024-02-29 16:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True
            ),
        ),
    ]

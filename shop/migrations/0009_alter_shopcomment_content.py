# Generated by Django 4.2 on 2024-02-26 06:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0008_remove_shopgallery_image_remove_shopgallery_video_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopcomment",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 4.2 on 2024-02-21 06:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="total_price",
        ),
    ]

# Generated by Django 4.2 on 2024-02-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financial", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]

# Generated by Django 4.2 on 2023-04-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0006_remove_child_parent_remove_cow_farmer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="family",
            name="cows",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
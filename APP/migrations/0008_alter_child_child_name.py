# Generated by Django 4.2 on 2023-04-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0007_alter_family_cows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="child",
            name="child_name",
            field=models.CharField(max_length=100),
        ),
    ]
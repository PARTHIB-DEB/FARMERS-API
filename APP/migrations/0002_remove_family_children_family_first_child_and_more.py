# Generated by Django 4.2 on 2023-04-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="family",
            name="Children",
        ),
        migrations.AddField(
            model_name="family",
            name="First_child",
            field=models.CharField(default="XYZ", max_length=100),
        ),
        migrations.AddField(
            model_name="family",
            name="Second_child",
            field=models.CharField(default="XYZ", max_length=100),
        ),
        migrations.AddField(
            model_name="family",
            name="Third_child",
            field=models.CharField(default="XYZ", max_length=100),
        ),
        migrations.DeleteModel(
            name="child",
        ),
    ]

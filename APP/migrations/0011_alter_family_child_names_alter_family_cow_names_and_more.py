# Generated by Django 4.2 on 2023-04-23 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0010_alter_family_child_names_alter_family_cow_names_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="family",
            name="child_names",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="child_names",
                to="APP.child",
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="cow_names",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cow_names",
                to="APP.cow",
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="goat_names",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="goat_names",
                to="APP.goat",
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="sheap_names",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sheap_names",
                to="APP.sheap",
            ),
        ),
    ]

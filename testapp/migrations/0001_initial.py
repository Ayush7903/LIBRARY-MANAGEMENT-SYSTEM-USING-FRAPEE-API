# Generated by Django 4.2.4 on 2023-08-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_of_book", models.CharField(max_length=500)),
                ("name_of_author", models.CharField(max_length=500)),
            ],
        ),
    ]
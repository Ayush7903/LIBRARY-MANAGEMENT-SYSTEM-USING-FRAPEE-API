# Generated by Django 4.2.4 on 2023-08-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0005_alter_book_curr_availability"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="user_name",
            field=models.CharField(default="user.default", max_length=500),
            preserve_default=False,
        ),
    ]

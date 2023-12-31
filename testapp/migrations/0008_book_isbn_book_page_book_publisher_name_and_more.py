# Generated by Django 4.2.4 on 2023-08-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0007_alter_member_date_of_book_issued"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="isbn",
            field=models.CharField(default="##", max_length=500),
        ),
        migrations.AddField(
            model_name="book",
            name="page",
            field=models.CharField(default="0", max_length=500),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher_name",
            field=models.CharField(default="None", max_length=500),
        ),
        migrations.AlterField(
            model_name="book",
            name="Curr_availability",
            field=models.IntegerField(default=0),
        ),
    ]

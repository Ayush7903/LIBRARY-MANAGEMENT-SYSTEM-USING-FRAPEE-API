# Generated by Django 4.2.4 on 2023-08-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0012_alter_member_date_of_book_issued"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="Date_of_return",
            field=models.CharField(default="NOT RETURNED", max_length=500),
        ),
        migrations.AddField(
            model_name="member",
            name="Paid_amount",
            field=models.IntegerField(default=0),
        ),
    ]

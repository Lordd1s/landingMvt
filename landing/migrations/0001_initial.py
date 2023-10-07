# Generated by Django 4.2.5 on 2023-10-03 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("surname", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("email", models.EmailField(max_length=50, verbose_name="Почта")),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                ("address", models.CharField(max_length=50, verbose_name="Адрес")),
                (
                    "theme",
                    models.CharField(max_length=50, verbose_name="Тема обращений"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 10, 3, 4, 20, 7, 316382, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name": "Обращения",
                "verbose_name_plural": "Обращении",
                "ordering": ["-date_created", "-first_name"],
            },
        ),
    ]

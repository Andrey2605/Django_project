# Generated by Django 5.1.6 on 2025-03-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Введите страну проживания",
                max_length=40,
                null=True,
                verbose_name="Страна",
            ),
        ),
    ]

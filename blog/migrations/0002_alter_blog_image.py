# Generated by Django 5.1.6 on 2025-03-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media/image",
                verbose_name="Изображение",
            ),
        ),
    ]

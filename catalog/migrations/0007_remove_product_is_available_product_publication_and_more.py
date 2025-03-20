# Generated by Django 5.1.6 on 2025-03-18 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="is_available",
        ),
        migrations.AddField(
            model_name="product",
            name="publication",
            field=models.BooleanField(default=False, verbose_name="Статус публикации"),
        ),
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="имя владельца",
            ),
        ),
    ]

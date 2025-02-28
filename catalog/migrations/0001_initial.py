# Generated by Django 5.1.6 on 2025-02-23 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "names",
                    models.CharField(
                        help_text="Введите наименование",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="catalog/images",
                        verbose_name="Изображение",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "updated_at",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["names", "category"],
            },
        ),
    ]

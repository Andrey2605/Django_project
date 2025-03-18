from django.db import models

from config import settings
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )  # наименование,
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True
    )  # описание,

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    names = models.CharField(
        max_length=100, verbose_name="Наименование"
    )  # наименование,
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True
    )  # описание,
    image = models.ImageField(
        upload_to="media/images", blank=True, null=True, verbose_name="Изображение"
    )  # изображение,
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )  # категория,
    price = models.IntegerField(verbose_name="Цена")  # цена за покупку,
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания"
    )  # дата создания,
    updated_at = models.DateField(
        auto_now_add=True, verbose_name="Дата последнего изменения"
    )  # дата последнего изменения.
    publication = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(
        CustomUser,
        verbose_name="имя владельца",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["names", "category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("remove_any_product", "Remove any product"),
        ]

    def __str__(self):
        return self.names

# Generated by Django 5.1.6 on 2025-03-18 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_names"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["names", "category"],
                "permissions": [("can_unpublish_product", "Can unpublish product")],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]

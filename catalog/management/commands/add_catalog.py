from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test catalog to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="Фрукты")

        Products = [
            {"names": "Апельсин", "price": "51", "category": category},
            {"names": "Виноград", "price": "65", "category": category},
        ]

        for product_data in Products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.names}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.names}")
                )

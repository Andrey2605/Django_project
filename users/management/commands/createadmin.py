from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email="andy@mail.ru", first_name="Andy", last_name="Drea"
        )
        user.set_password("andy2605")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user with email {user.email}"
            )
        )

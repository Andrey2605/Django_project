from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(
        max_length=40,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите страну проживания",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

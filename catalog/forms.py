from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

forbidden = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["names", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["names"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите названия продукта",  # Текст подсказки внутри поля
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Описание продукта",  # Текст подсказки внутри поля
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
            }
        )

        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Укажите цену",  # Указание типа поля как даты
            }
        )

    def clean(self):
        names = self.cleaned_data.get("names")
        description = self.cleaned_data.get("description")
        for word in forbidden:
            if word in names.lower() or word in description.lower():
                raise ValidationError(
                    "Название и описание не должны содержать запрещенные слова."
                )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")

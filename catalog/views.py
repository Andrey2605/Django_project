from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ["names", "description", "image", "category", "price"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["names", "description", "image", "category", "price"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


class ContactTemplateView(TemplateView):
    template_name = "contacts.html"

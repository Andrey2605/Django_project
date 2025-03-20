from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Category, Product
from catalog.servise import get_products_by_category, get_products_from_cache


def my_view(request):
    # Попытка получить данные из кеша
    data = cache.get("my_key")

    # Если данные не найдены в кеше, выполняем вычисления и сохраняем результат в кеш
    if not data:
        data = "some expensive computation"
        cache.set("my_key", data, 60 * 15)  # Кешируем данные на 15 минут

    # Возвращаем ответ с данными
    return HttpResponse(data)


class UnpublishedProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав отмены публикации.")

        product.publication = False
        product.save()

        return redirect("catalog:product_detail", pk=product_id)


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        return get_products_from_cache()


class ProductsByCategoryView(ListView):
    model = Category
    template_name = "catalog/home.html"
    context_object_name = "products_by_category"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        return get_products_by_category(category_id=category_id)


class CategoryListView(ListView):
    model = Category


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user and not user.has_perm("catalog.product_delete"):
            raise PermissionDenied("Вы не можете удалять этот продукт.")

        return product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

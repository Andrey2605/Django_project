from itertools import product

from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context=context)


def contacts(request):
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context=context)

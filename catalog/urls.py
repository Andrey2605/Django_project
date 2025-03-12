from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactTemplateView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductsListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductsListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

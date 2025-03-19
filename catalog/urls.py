from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ContactTemplateView,
                           ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductsByCategoryView,
                           ProductsListView, ProductUpdateView,
                           UnpublishedProductView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductsListView.as_view(), name="home"),
    path(
        "product/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/unpublished_product_views/<int:product_id>/",
        UnpublishedProductView.as_view(),
        name="unpublished_product_views",
    ),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path(
        "category/<int:pk>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

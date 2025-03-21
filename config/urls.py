from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("", include("blog.urls", namespace="blog")),
    path("users/", include("users.urls", namespace="users")),
]

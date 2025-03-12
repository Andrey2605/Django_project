from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    context_object_name = "blog"

    def get_queryset(self):
        # Получаем только активные объекты
        return Blog.objects.filter(publication=True)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "image",
    )
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ("title", "content", "image")
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")

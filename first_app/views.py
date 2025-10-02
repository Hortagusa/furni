from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView

from .models import About, Blog, Shop


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(ListView):
    template_name = "about.html"
    model = About
    context_object_name = "abouts"


class AboutDetailView(DetailView):
    template_name = "about_detail.html"
    model = About
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["abouts"] = About.objects.all()
        return context


class AboutUpdateView(UpdateView):
    fields = ("image", "name", "position", "description", "content")
    model = About
    success_url = reverse_lazy("about")


class AboutCreateView(CreateView):
    fields = ("image", "name", "position", "description", "content")
    model = About
    success_url = reverse_lazy("about")


class AboutDeleteView(DeleteView):
    model = About
    success_url = reverse_lazy("about")


class BlogView(ListView):
    template_name = "blog.html"
    model = Blog
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    template_name = "blog_detail.html"
    model = Blog
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context


class BlogUpdateView(UpdateView):
    fields = ("image", "name", "content")
    model = Blog
    success_url = reverse_lazy("blog")


class BlogCreateView(CreateView):
    fields = ("image", "name", "content")
    model = Blog
    success_url = reverse_lazy("blog")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog")


class ShopView(ListView):
    template_name = "shop.html"
    context_object_name = "shops"
    model = Shop


class ShopDetailView(DetailView):
    model = Shop
    template_name = "shop_detail.html"
    context_object_name = "shop_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shops"] = Shop.objects.all()
        return context


class ShopUpdateView(UpdateView):
    fields = ("image", "name", "price", "description")
    model = Shop
    success_url = reverse_lazy("shop")


class ShopCreateView(CreateView):
    fields = ("image", "name", "price", "description")
    model = Shop
    success_url = reverse_lazy("shop")


class ShopDeleteView(DeleteView):
    model = Shop
    success_url = reverse_lazy("shop")


class CartView(TemplateView):
    template_name = "cart.html"


class CheckoutView(TemplateView):
    template_name = "checkout.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class ThankyouView(TemplateView):
    template_name = "thankyou.html"

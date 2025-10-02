"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from first_app import views

app_name = "first_app"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('thankyou/', views.ThankyouView.as_view(), name='thankyou'),

    path('about/<int:pk>/', views.AboutDetailView.as_view(), name='about_detail'),
    path("about/create/", views.AboutCreateView.as_view(), name="about_create"),
    path("about/<int:pk>/update/", views.AboutUpdateView.as_view(), name="about_update"),
    path("about/<int:pk>/delete/", views.AboutDeleteView.as_view(), name="about_delete"),

    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog_delete"),

    path('shop/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path("shop/create/", views.ShopCreateView.as_view(), name="shop_create"),
    path("shop/<int:pk>/update/", views.ShopUpdateView.as_view(), name="shop_update"),
    path("shop/<int:pk>/delete/", views.ShopDeleteView.as_view(), name="shop_delete"),
]

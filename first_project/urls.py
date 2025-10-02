from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.IndexView.as_view(), name='index'),

    # Shop
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path("shop/create/", views.ShopCreateView.as_view(), name="shop_create"),
    path("shop/<int:pk>/update/", views.ShopUpdateView.as_view(), name="shop_update"),
    path("shop/<int:pk>/delete/", views.ShopDeleteView.as_view(), name="shop_delete"),

    # About
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/<int:pk>/', views.AboutDetailView.as_view(), name='about_detail'),
    path("about/create/", views.AboutCreateView.as_view(), name="about_create"),
    path("about/<int:pk>/update/", views.AboutUpdateView.as_view(), name="about_update"),
    path("about/<int:pk>/delete/", views.AboutDeleteView.as_view(), name="about_delete"),

    # Blog
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog_delete"),

    # Static pages
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('thankyou/', views.ThankyouView.as_view(), name='thankyou'),
]

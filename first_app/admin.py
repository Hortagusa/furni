from django.contrib import admin

from first_app.models import Product, Shop, About, Blog

# Register your models here.
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(About)
admin.site.register(Blog)

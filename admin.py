from django.contrib import admin
from .models import Blog, Supplier, Product,Order

admin.site.register(Blog)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Order)
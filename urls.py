from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-list/', views.product_list, name='product_list'),  # Add this path
    path('search/', views.product_search, name='product_search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order/<int:product_id>/', views.place_order, name='order_product'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]

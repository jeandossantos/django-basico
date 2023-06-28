from django.urls import path
from . import views

urlpatterns = [
    path('show_products', views.show_products, name='show_products'),
    path('add_products', views.add_product, name='add_product')
]


from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('warehouses/', views.WarehouseList.as_view(), name='warehouse-list'),
]

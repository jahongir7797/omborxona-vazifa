# views.py

from rest_framework import generics
from .models import Product, Warehouse
from myapp.serializers import ProductSerializer, WarehouseSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WarehouseList(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


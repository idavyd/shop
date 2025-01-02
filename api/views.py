from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class GeneralProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GeneralCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

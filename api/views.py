from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
import requests
from django.core.files.base import ContentFile

class GeneralProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GeneralCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        # Check if the request contains an image URL
        icon_url = self.request.data.get('icon_url', None)

        if icon_url:
            # If an icon URL is provided, download and save the image
            response = requests.get(icon_url)
            if response.status_code == 200:
                # Save the image as a file object
                icon_image = ContentFile(response.content)
                # Save the image file to the category instance
                category = serializer.save(icon=icon_image)
            else:
                # Handle error if the image could not be fetched
                raise Exception("Image URL could not be fetched.")
        else:
            # If no icon URL is provided, save the category normally
            serializer.save()
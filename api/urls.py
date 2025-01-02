from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('list_prods/', GeneralProductView.as_view(), name='all_products'),
    path('list_categories/', GeneralCategoryView.as_view(), name='all_categories')
]

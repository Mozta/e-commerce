
from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='products'),
    path('create', CreateProduct.as_view(), name='create_product'),
]

from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='products'),
    path('create', CreateProduct.as_view(), name='create_product'),
    path('update/<int:id>', UpdateProduct.as_view(), name='update_product'),
    path('delete/<int:id>', DeleteProduct.as_view(), name='delete_product')
]
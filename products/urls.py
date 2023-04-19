
from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='products'),
]
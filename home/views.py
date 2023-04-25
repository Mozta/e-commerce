from django.shortcuts import render
from django.views import View
from products.models import Product
# Create your views here.
class Home(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'index.html', context)
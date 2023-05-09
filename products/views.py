from django.shortcuts import redirect, render
from django.views import View
from .models import Product
from .forms import ProductCreate

# Create your views here.


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products/products.html', context)


class CreateProduct(View):
    def get(self, request):
        form = ProductCreate()
        context = {'form': form}
        return render(request, 'products/form.html', context)

    def post(self, request):
        form = ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("FORM ERROR!")
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/form.html', context)


class UpdateProduct(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(instance=product)
        context = {'form': form}
        return render(request, 'products/update_form.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("FORM UPDATE ERROR!")
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/update_form.html', context)


class DeleteProduct(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('products')
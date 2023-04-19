from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        context = {'products': ['Teléfonos desbloqueados', 'Carteras', 'Laptops', 'Mochilas']}
        return render(request, 'index.html', context)
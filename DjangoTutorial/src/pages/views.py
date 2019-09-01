from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    context = { 'products' : Product.objects.all() }
    return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
    print(request.user)

    return render(request, "contact.html")

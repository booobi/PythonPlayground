from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import RawProductForm
from .forms import ProductForm
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    return render(request, "products/product_detail.html", {'obj':obj})

# def product_create_view(request):
#     context = {}

#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form':form
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    context = {}
    initial_data = {
            'title': 'This is an awesome title'
    }
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, initial = initial_data, instance = obj)
    if form.is_valid():
        form.save()
        form=ProductForm()
    
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = { "object":obj }

    return render(request, "products/product_detail.html", context)
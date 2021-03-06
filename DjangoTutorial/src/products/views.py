from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import RawProductForm
from .forms import ProductForm
# Create your views here.

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = { "object":obj }

    return render(request, "products/product_detail.html", context)

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
    # obj = Product.objects.get(id=3) #TODO: add edit view
    form = ProductForm(request.POST or None, initial = initial_data)
    if form.is_valid():
        form.save()
        form=ProductForm()
    
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = { "object":obj }
    if request.method == "POST":
        obj.delete()
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "products/product_list.html", context)
from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    return render(request, "products/product_detail.html", {'obj':obj})

def product_create_view(request):
    form = ProductForm(request.POST or None)
    objs = Product.objects.all();
    if(form.is_valid()):
        form.save()

    return render(request, "products/product_create.html", {'form':form, 'products':objs})
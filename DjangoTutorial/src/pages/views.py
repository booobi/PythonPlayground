from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    print(request.user)
    my_context = {"my_text":"This is my text", 
    "products": [1,2,3,4,5],
    "my_html": "<h1>haha</h1>"
    }
    
    return render(request, "contact.html", my_context)

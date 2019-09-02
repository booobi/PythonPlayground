from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    context = {}
    return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
    print(request.user)

    return render(request, "contact.html")

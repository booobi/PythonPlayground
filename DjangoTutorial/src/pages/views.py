from django.shortcuts import render
from django.views import View
# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    context = {}
    return render(request, "home.html", context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, "contact.html")

    def post(self, request, *args, **kwargs):
        print(request.user)
        return render(request, "contact.html")



from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def fields(request):
    return render(request, "pages/fields.html", {})

def accessories(request):
    return render(request, "pages/accessories.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})
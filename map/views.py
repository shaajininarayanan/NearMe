from django.shortcuts import render

def home(request):
    return render(request, "map.html")

def beach(request):
    return render(request, "beach.html")

def fort(request):
    return render(request, "fort.html")

def college(request):
    return render(request, "college.html")
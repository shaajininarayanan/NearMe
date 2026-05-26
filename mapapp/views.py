from django.shortcuts import render

def map_page(request):
    return render(request, "mapapp/map.html")

def beach(request):
    return render(request, "mapapp/beach.html")

def fort(request):
    return render(request, "mapapp/fort.html")

def college(request):
    return render(request, "mapapp/college.html")
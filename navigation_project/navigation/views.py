from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("navigation home page")
def contact(request):
    return render(request,"navigation/contact.html")
def about(request):
    return render(request,"navigation/about.html")

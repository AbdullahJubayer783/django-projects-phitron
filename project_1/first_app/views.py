from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'first_app/first_app_index.html')

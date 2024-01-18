from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    dict = {'author' : 'mahin' , 'age' : 25 , 'lst' : [1,2,3,4,5,6,76,7], 'courses':[
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 1000
        },
        {
            'id' : 2,
            'name' : 'c/c++',
            'fee' : 2000
        },
        {
            'id' : 3,
            'name' : 'django',
            'fee' : 3500
        }
    ]}
    return render(request,'first_app/home.html' ,  dict)
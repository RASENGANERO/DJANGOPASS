from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/index.html")

def documentation(request):
    return render(request,"generator/documentation.html")

def password(request):
    #print(request)
    thepassword=''
    
    characters=list('qwertyuiopasdfghjklzxcvbnm')
    
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+;:?_=,/'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length=int(request.GET.get('length',11))
    
    for v in range(length):
        thepassword+=random.choice(characters)
    
    return render(request,"generator/password.html",{"password":thepassword})
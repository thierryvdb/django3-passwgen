from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    #return HttpResponse("Hello There")
    return render(request,'guinesmecanico/home.html',{'password':'123456'})


def password(request):
    
    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()-_=+^~:?<>,.'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))        
        
        
    length=int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
        
        
    return render(request,'guinesmecanico/password.html', {'password':thepassword})



from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    person = {'name' : 'amir'}
    return render(request , 'hello' , context=person)

#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def add(request,a,b):
    a = request.GET.get("a",0)
    b = request.GET.get("b",0)
    c = int(a)+int(b)
    return HttpResponse(str(c))


#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return render(request, "index.html")

def add(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


#coding:utf-8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def search_form(request):
    return  render_to_response("search_form.html")

def search(request):
    request.encoding = "utf-8"
    if "keyword" in request.GET:
        message = "你搜索的内容为：" + request.GET["keyword"]
    else:
        message = "你提交了空信息"
    return  HttpResponse(message)

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST["keyword"]
    return render(request, "post.html", ctx)
# 执行响应的逻辑代码模块；
# 代码逻辑处理的主要地点。
from django.shortcuts import render
from django.http import HttpResponse

# Django中，所有的请求都需要函数处理；
def index(request):
    return HttpResponse("Hello, world!")


# Create your views here.

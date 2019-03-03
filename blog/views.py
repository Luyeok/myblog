# 执行响应的逻辑代码模块；
# 代码逻辑处理的主要地点。
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Django中，所有的请求都需要函数处理；
def index(request):
    articles = models.Article.objects.all()
    # 这里，objects.all()返回的是一个查询的集合对象；
    return render(request, 'blog/index.html', {'articles': articles})


# Create your views here.

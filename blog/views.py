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

def article_page(request,article_id):
    article= models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request, article_id):
    if str(article_id)=="0":
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html', {'article': article})

def edit_action(request):
    title= request.POST.get('title', 'TITLE')
    content=request.POST['content']
    article_id =request.POST.get('article_id','0')
    if article_id=='0':
    #这里是两种取字典数据的方法，第一种，默认值是'TITLE'
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article=models.Article.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(request,'blog/article_page.html',{'article':article})


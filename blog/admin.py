# 当前应用（blog）的后台管理系统配置文件；
# Django自带一个后台管理系统，每一个应用下，都有一个配置文件。

from django.contrib import admin
from blog.models import Article

# Admin 配置类
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','content','pub_time')
    list_filter = ('pub_time', )

admin.site.register(Article, ArticleAdmin)

# Register your models here.

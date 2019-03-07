# 数据模型模块，使用ORM框架；
# 类似MVC结构中的models
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default="Title")
    content= models.TextField(null=True)
    pub_time=models.DateTimeField(null=True)

    def __str__(self):
        return self.title
# 这里，我们通过article自身的动作设置，来打印需要的信息。
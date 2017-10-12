from django.db import models

class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']

class User(models.Model):
    userName = models.CharField(max_length=50)#用户姓名
    passWord = models.CharField(max_length=50)#密码
    userType = models.CharField(max_length=10)#用户类别

    def __str__(self):
        return self.userName
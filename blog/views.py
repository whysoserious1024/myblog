from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.decorators import csrf
from blog.models import Article,User

import time

# Create your views here.
def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExits:
        return Http404
    return render(request,'article.html',{'post':post})

def home(request):
    post_list = Article.objects.all()
    return render(request,'index.html',{'post_list':post_list})

def userinfo(request):
    user_list = User.objects.all()
    return render(request,'userinfo.html',{'user_list':user_list})

def writeBlog(request):
    return render(request,'writeblog.html')

def articlePost(request):
    con = {}
    if request.POST :
        con['title'] = request.POST['title']
        con['category'] = request.POST['category']
        con['content'] = request.POST['content']
        Article.objects.create(**con)
    return HttpResponseRedirect('/')
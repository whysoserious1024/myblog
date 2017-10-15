from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template.context import RequestContext
from django.views.decorators import csrf
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from blog.models import Article
import time


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})
    else:
        return render(request,'login.html',{'msg':''})



def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExits:
        return Http404
    return render(request,'article.html',{'post':post})

def home(request):
    username = request.session.get('username')
    if username:
        post_list = Article.objects.all()
        return render(request,'index.html',{'post_list':post_list})
    else:
        return HttpResponseRedirect("/login/")


def editBlog(request,id):
    try:
        post = Article.objects.get(id=str(id))
        return render(request,'writeblog.html',{'post':post})
    except Article.DoesNotExits:
        return Http404

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
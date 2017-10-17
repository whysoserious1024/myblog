from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExits:
        return Http404
    return render(request,'article.html',{'post':post})

@login_required
def home(request):
    post_list = Article.objects.all()
    # print(post_list)
    # for post in post_list:
    #     print(type(post.all()))
    return render(request,'index.html',{'post_list':post_list})


@login_required
def editBlog(request,id):
    try:
        post = Article.objects.get(id=str(id))
        return render(request,'writeblog.html',{'post':post})
    except Article.DoesNotExits:
        return Http404

@login_required
def writeBlog(request):
    return render(request,'writeblog.html')

@login_required
def articlePost(request):
    con = {}
    if request.POST :
        con['title'] = request.POST['title']
        con['category'] = request.POST['category']
        con['content'] = request.POST['content']
        if (request.POST['id']):
            con['id'] = request.POST['id']
            Article.objects.filter(id=str(con['id'])).update(**con)
        else:
            Article.objects.create(**con)
    return HttpResponseRedirect('/')
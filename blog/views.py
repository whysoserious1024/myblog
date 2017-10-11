from django.shortcuts import render
from django.http import HttpResponse,Http404
from blog.models import Article

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
from django.shortcuts import render,HttpResponse
from Home.models import Catergory, Post


def home(request):
    post = Post.objects.all()[:5]
    cat = Catergory.objects.all()
    blogs = {
        'post' : post,
        'cat': cat
    }
    return render(request,'home.html',blogs)

def post(request,url):
    post = Post.objects.get(url=url)
    return render(request,'Post.html',{'post':post})
from django.shortcuts import render
from .models import *
from .forms import CommentForm

def blog(request):
    posts=Post.objects.all().order_by('-created_on')
    context={
        'posts':posts
    }
    return render(request,'blog.html',context)


def detail(request,pk):
    post=Post.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    context={
        'post':post,
        # 'comments':comments
    }
    return render(request,'details.html',context)
# Create your views here.


def comment(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments=Comment.objects.filter(post=post)
    context={
        'post':post,
        'form':form,
        'comments':comments
    }
    return render(request,'details.html',context)

def index(request):
    return render(request,'index.html',{})

def chat(request):
    return render(request,'chat.html',{})
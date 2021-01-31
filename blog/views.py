from django.shortcuts import render
from .models import Post

# Create your views here.

def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'blog/index.html',context)


def Detail(request, pk):

  post = Post.objects.get(id=pk)
  context =  {'post':post}

  return render(request,'blog/detail.html',context)
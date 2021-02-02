from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

# Home View 
def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'blog/index.html',context)

# Detail View 
def Detail(request, id):

  post = Post.objects.get(id=id)
  context =  {'post':post}

  return render(request,'blog/detail.html',context)



#Create View
def Create(request):
  user = User
  if request.method == 'POST':
    post = Post(
      title = request.POST['title'],
      body  = request.POST['body'],
      postImage = request.FILES['image'],
      author = request.user
    )
    post.save()
    return redirect('/')
    

  return render(request,'blog/create.html')



# Upudate View

""" def Update(request, id):
  post = Post.objects.get(id=id)
  context = {'post':post}
  if request.method == 'POST':
    post.title = request.POST['title']
    post.body  = request.POST['body']
    post.postImage = request.FILES['image']

    post.save()
    return redirect('/')

  return render(request,'blog/update.html',context)
 

 """
""" 
def Delete(request, id):
  post = Post.objects.get(id=id)
  post.delete()

  return render(request,'blog/index.html')
   """

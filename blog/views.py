from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

# Create your views here.

# Home View 
def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'blog/index.html',context)

# Detail View 
def PostDetail(request, id):

  post = Post.objects.get(id=id)
  comments = Comment.objects.filter(post=post).order_by('-id')
  likes  = post.likes.count()
  context =  {'post':post,'comments':comments,'likes':likes}
  if request.method == 'POST':
    content = request.POST['content']
    comment = Comment.objects.create(content=content,user=request.user,post=post)
    print(comment)
    """ comment.save()
    return redirect('/') """


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




def likes(request, pk):
  
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
  else:
     post.likes.add(request.user)
  
  return redirect('/detail/'+str(post.id))

  



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

from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from blog.forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    form = PostForm()
    return render(request, 'blog/post_list.html', {'form': form, 'posts': posts})

@login_required
def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
        return redirect('blog.views.post_list')
    

def logout_view(request):
    logout(request)
    return redirect('blog.views.post_list')
       

@login_required
def post_del(request, pk):
  post = get_object_or_404(Post, pk=pk)
  try:
    post.delete()
    return redirect('blog.views.post_list')
  except Exception as e:
      return redirect('blog.views.post_edit', {'pk':pk})

@login_required
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
        return redirect('blog.views.post_list')
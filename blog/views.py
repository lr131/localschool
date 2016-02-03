from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.files import File
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from blog.forms import PostForm, RaspForm, UploadFileForm
from .models import Post, Rasp

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
    
#@login_required
def rasp_list(request):
    form = RaspForm()
    return render(request, 'blog/raspisanie.html', {'form': form})

def rasp_list(request):
    return render(request, 'blog/raspisanie.html')

def table_list(request):
    return render(request, 'blog/table.html')

def rasp_change(request):
    return render(request, 'blog/101.html')

def rasp_zv(request):
    return render(request, 'blog/zv_all.html')

def plan_page(request):
    form = UploadFileForm()
    return render(request, 'blog/plan_page.html', {'form': form})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
    return redirect('blog.views.plan_page')
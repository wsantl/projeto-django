from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, './home.html', {'posts': posts})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para uma página de lista de posts (substitua com a URL desejada)
    else:
        form = PostForm()

    return render(request, 'criar_post.html', {'form': form})
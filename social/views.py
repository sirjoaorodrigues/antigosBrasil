from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            Profile.objects.create(user=user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def feed(request):
    posts = Post.objects.prefetch_related('comments__user').all()
    
    if request.method == 'POST':
        if 'post_form' in request.POST:
            form_post = PostForm(request.POST, request.FILES)
            if form_post.is_valid():
                post = form_post.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('feed')
        
        elif 'comment_form' in request.POST:
            form_comment = CommentsForm(request.POST)
            if form_comment.is_valid():
                comment = form_comment.save(commit=False)
                comment.user = request.user
                comment.post_id = request.POST.get('post_id')
                comment.save()
                return redirect('feed')
    
    # Create empty forms for GET request
    form_post = PostForm()
    form_comment = CommentsForm()
    
    context = {
        'posts': posts,
        'form_post': form_post,
        'form_comment': form_comment,
    }
    return render(request, 'feed.html', context)
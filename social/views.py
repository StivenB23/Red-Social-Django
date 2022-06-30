from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
# Create your views here.
def feed(request):
    post = Post.objects.all()
    context={'posts': post}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        #campos que fueron llenados
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        #mostrar formulario vacio    
        form = UserRegisterForm()
    context= {'form':form}
    return render(request,'social/register.html',context)

def post(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Enviado')
            return redirect('feed')
        else:
            form = PostForm()
            return render(request, 'social/post.html',{'form':form})

def profile(request):
    return render(request, 'social/profile.html');
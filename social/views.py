from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request, 'social/feed.html');

def profile(request):
    return render(request, 'social/profile.html');
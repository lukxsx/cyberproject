from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Thread

# Create your views here.
def index(request):
    thread_list = Thread.objects.order_by('-thread_date')[:5]
    context = {
        'thread_list': thread_list,
    }
    return render(request, 'index.html', context)

def threadview(request, thread_id):
    post_list = Post.objects.filter(thread=thread_id).order_by('post_date')
    return render(request, 'thread.html', {'post_list': post_list})
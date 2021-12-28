from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Thread
from django.utils import timezone

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
    

def addthread(request):
	if request.method == 'GET':
		title = request.GET.get('title')
		nt = Thread(thread_title=title, thread_date=timezone.now())
		nt.save()
	
	thread_list = Thread.objects.order_by('-thread_date')[:5]
	context = {
		'thread_list': thread_list,
	}
	return render(request, 'index.html', context)

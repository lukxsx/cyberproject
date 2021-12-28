from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Thread
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	thread_list = Thread.objects.order_by('-thread_date')[:5]
	context = {
		'thread_list': thread_list,
	}
	return render(request, 'index.html', context)

def threadview(request, thread_id):
    t = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'thread.html', {'thread': t})
    

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

def addpost(request, thread_id):
	t = get_object_or_404(Thread, pk=thread_id)
	message = request.POST['message']
	p = Post(post_text=message, post_date=timezone.now(), thread=t)
	p.save()
	
	return HttpResponseRedirect(reverse('threadview', args=(t.id,)))


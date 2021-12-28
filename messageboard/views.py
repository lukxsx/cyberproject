from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Thread
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'login.html', {'error': "Wrond username or password"})
	else:
		return render(request, 'login.html', {'error': "You need to login first."})
		
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login/')
def index(request):
	thread_list = Thread.objects.order_by('-thread_date')[:5]
	context = {
		'thread_list': thread_list,
	}
	return render(request, 'index.html', context)

@login_required(login_url='login/')
def threadview(request, thread_id):
    t = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'thread.html', {'thread': t})
    
@login_required(login_url='login/')
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

@login_required(login_url='login/')
def addpost(request, thread_id):
	t = get_object_or_404(Thread, pk=thread_id)
	message = request.POST['message']
	p = Post(post_text=message, post_date=timezone.now(), thread=t)
	p.save()
	
	return HttpResponseRedirect(reverse('threadview', args=(t.id,)))


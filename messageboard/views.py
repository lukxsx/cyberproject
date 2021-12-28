from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Thread
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def register_view(request):
	if request.method == 'POST':
		username = request.POST['username']

		if len(User.objects.raw('SELECT * FROM auth_user WHERE username="' + username + '"')) >= 1:
			return render(request, 'register.html', {'error': "Username already in use."})
			
		password = request.POST['password']
		password_verify = request.POST['password_verify']
		if password != password_verify:
			return render(request, 'register.html', {'error': "Passwords don't match."})
		user = User.objects.create_user(username, None, password)
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'register.html')

@csrf_exempt
@login_required(login_url='login/')
def index(request):
	thread_list = Thread.objects.order_by('-thread_date')[:5]
	context = {
		'thread_list': thread_list,
	}
	return render(request, 'index.html', context)

@csrf_exempt
@login_required(login_url='login/')
def threadview(request, thread_id):
    t = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'thread.html', {'thread': t},)
    
@csrf_exempt
@login_required(login_url='login/')
def addthread(request):
	if request.method == 'GET':
		title = request.GET.get('title')
		message = request.GET.get('message')
		timenow = timezone.now()
		nt = Thread(thread_title=title, thread_date=timenow, thread_user=request.user)
		nt.save()
		ps = Post(post_text=message, post_date=timenow, thread=nt, post_user=request.user)
		ps.save()
	
	thread_list = Thread.objects.order_by('-thread_date')[:5]
	context = {
		'thread_list': thread_list,
	}
	return render(request, 'index.html', context)

@csrf_exempt
@login_required(login_url='login/')
def addpost(request, thread_id):
	t = get_object_or_404(Thread, pk=thread_id)
	message = request.POST['message']
	p = Post(post_text=message, post_date=timezone.now(), thread=t, post_user=request.user)
	p.save()
	
	return HttpResponseRedirect(reverse('threadview', args=(t.id,)))


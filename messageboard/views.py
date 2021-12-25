from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-post_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

def postview(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post_text': post})
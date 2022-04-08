from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Post
from .forms import EditPostForm

# Create your views here.

def index(request):
	post_list = Post.objects.order_by('-pub_date')
	context = {
		'post_list': post_list,
	}
	return render(request, 'blog/index.html', context)


def view_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {
		'post': post,
	}
	return render(request, 'blog/view_post.html', context)

def new_post(request):
	return render(request, 'blog/new_post.html')

def create_post(request):
	error_messages = []
	
	title = request.POST['title']
	body = request.POST['body']

	if title == '':
		error_messages.append("Please enter a title.")
	if body == '':
		error_messages.append("Body cannot be empty.")

	if len(error_messages) > 0:
		return render(request, 'blog/new_post.html', {
				'error_messages': error_messages,
			})
	else:
		new_post = Post(title=title, body=body, pub_date=timezone.now())
		new_post.save()
		return HttpResponseRedirect(reverse('blog:index'))

def edit_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	form = EditPostForm(initial={'title': post.title, 'body': post.body, 'pub_date': post.pub_date})
	return render(request, 'blog/edit_post.html', {
			'post': post,
			'form': form,
		})

"""def update_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	POSTcopy = request.POST.copy()
	POSTcopy.update({'pub_date': post.pub_date.strftime('%m/%d/%Y')})
	form = EditPostForm(POSTcopy)
	form.pub_date = post.pub_date #.strftime('%m/%d/%Y')
	if form.is_valid():
		return Http404()
	else:
		return render(request, 'blog/edit_post.html', {
				'post': post,
				'form': form,
				'POST': POSTcopy,
				})"""
		
def update_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	form = EditPostForm(request.POST)
	if form.is_valid():
		post.title = form.cleaned_data['title']
		post.body = form.cleaned_data['body']
		post.pub_date = form.cleaned_data['pub_date']
		post.save()
		return HttpResponseRedirect(reverse('blog:view', kwargs={'post_id': post.id}))
	else:
		return render(request, 'blog/edit_post.html', {
				'post': post,
				'form': form,
				'POST': request.POST,
		})
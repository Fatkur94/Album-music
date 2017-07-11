from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .forms import PostForm
from .models import Post, Category

# Create your views here.

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'blog/category_list.html', {'categories':categories})


def post_list(request):
	posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	query = request.GET.get('q')
	if query:
		posts_list = posts_list.filter(
					Q(title__icontains=query)|
					Q(text__icontains=query)|
					Q(author__first_name__icontains=query)|
					Q(author__last_name__icontains=query)
					).distinct() # distinct = overriding duplicate items
	paginator = Paginator(posts_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)


	return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_create(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			messages.success(request, 'succesfully created')
			return redirect('blog:post_detail', post.pk)
		else:
			messages.error(request, ' not succesfully created')
	else:
		form = PostForm()
	context = {
		'form': form,
	}
	return render(request, 'blog/post_create.html', context)

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			messages.success(request, 'succesfully updated')
			return redirect('blog:post_detail', post.pk)
		else:
			messages.success(request, 'not succesfully created')
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('blog:post_list')

@login_required
def post_draft(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'blog/post_draft.html', {'posts':posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return redirect('blog:post_detail', post.pk)




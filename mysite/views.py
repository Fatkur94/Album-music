from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
import datetime
from books.models import *


def index(request):
	return HttpResponse('wellcome to the %s' % request.path)

def home(request):
	return render(request, 'blog/home.html', {})

#version 1
#def display_good1(request):
#	try:
#		ua = request.META['HTTP_USER_AGENT']
#	except KeyError:
#		ua = 'unknown'
#	return HttpResponse("Your browser is %s" % ua)

#version 2
def display_good2(request):
	ua = request.META.get('REMOTE_ADDR', 'unknown')
	return HttpResponse('this is a %s' % ua)

def display_meta(request):
	values = request.META.items()
	
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def current_datetime(request):
	now = datetime.datetime.now()

	return render(request, 'current_datetime.html', {'now':now})

def display_book(request):
	all = Books.objects.all()
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Please type in the search field')
		elif len(q) > 20:
			errors.append('Please type at least 20 character or shorter')
		else:
			book = Books.objects.filter(title__icontains=q)
			context = {
				'book': book,
				'query': q,
			}
			return render(request, 'search_result.html', context)
	context = { 'all':all,
				'errors':errors, }

	return render(request, 'book_list.html', context)


def hours_ahead(request, num):
	try:
		num = int(num)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now()
	ft = datetime.timedelta(hours=num)
	result = now + ft
	context = {
		'num':num,
		'result':result,
	}
	return render(request, 'hours_ahead.html', context)



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
					cd['subject'],
					cd['message'],
					cd.get('email', 'noreply@example.com'),
					['siteowner@example.com'],
					)
			return HttpResponseRedirect('/contact/thanks/')

	else:
		form = ContactForm(
			initial={'subject':'i love your site'})
	return render(request, 'contact_form.html', {'form':form})


#newmethodclassbasedgeneric
class PublisherList(ListView):
	model = Publisher
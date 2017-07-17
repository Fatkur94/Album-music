from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# Create your views here.
def portofolio_list(request):
	instance = Post_Portofolio.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'portofolio/portofolio_list.html', {'instance':instance})


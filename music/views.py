from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
	all_album = Album.objects.all()
	context = {
		'all_album': all_album,
	}
	return render(request, 'music/index.html', context)

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', { 'album':album, })

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['item'])
	except (KeyError, Song.DoesNotExist):
		context = {
			'album':album,
			'error_message': 'you didnt select favorite song',
		}
		return render(request, 'music/detail.html', context)

	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album':album })
from django import forms
#from pagedown.widgets import PagedownWidget
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorUploadingWidget())
	#text = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Post
		fields = ('title', 'image', 'text', 'category')


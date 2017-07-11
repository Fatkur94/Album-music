from django.db import models
from django.conf import settings
from django.utils import timezone
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

def image_location(instance, filename):
	return 'user_%s/%s' %(instance, filename)


class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to=image_location,
			null=True, blank=True,
			height_field='height_field',
			width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	text = RichTextUploadingField('text')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey(Category, verbose_name='Category', null=True, blank=True)

	def publish(self):
		self.published_date= timezone.now()
		self.save()

	def __str__(self):
		return self.title


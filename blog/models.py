from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

def image_location(instance, filename):
	return 'user_%s/%s' %(instance, filename)

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to=image_location,
			null=True, blank=True,
			height_field='height_field',
			width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date= timezone.now()
		self.save()

	def __str__(self):
		return self.title
from django.db import models
from django.utils import timezone
# Create your models here.

def image_location(instance, filename):
	return 'portofolio/%s/%s' %(instance.id, filename)


class Category(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Technology(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Post_Portofolio(models.Model):
	title = models.CharField(max_length=30)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_location, 
		height_field='height_field', 
		width_field='width_field',
		null=True, blank=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	technology = models.ManyToManyField('Technology')
	description = models.TextField(max_length=500)
	source = models.URLField(max_length=100)
	demo = models.URLField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

	def __str__(self):
		return self.title
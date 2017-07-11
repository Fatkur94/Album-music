from django.db import models

# Create your models here.

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
	technology = models.ManyToManyField('Technology')
	description = models.TextField(max_length=500)
	source = models.URLField(max_length=100)
	demo = models.URLField(max_length=100)

	def __str__(self):
		return self.title
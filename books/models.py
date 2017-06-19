from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	province = models.CharField(max_length=20)
	country = models.CharField(max_length=30)
	website = models.URLField()

	class Meta:
		ordering = ['-name']

	def __str__(self):
		return self.name

class Author(models.Model):
	f_name = models.CharField(max_length=20)
	l_name = models.CharField(max_length=30)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self):
		return '%s %s' %(self.f_name, self.l_name)

#Manager
#how to see number of title contains by 'django'
# run in the command = Books.objects.title_count('django')
class BooksManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

#class PeterBook(models.Manager):
#	def get_queryset(self):
#		return super(PeterBook, self).get_queryset().filter(penulis='Peter Thiel')

class Books(models.Model):
	title = models.CharField(max_length=50)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	pub_date = models.DateField(blank=True, null=True)

	objects = BooksManager()
	#peter_objects = PeterBook()

	def __str__(self):
		return self.title


#example to use models.Manager
#run in the command Person.People.all()
#run in the command Person.men.all()
#run in the command Person.women.all()

#class MaleManager(models.Manager):
#	def get_queryset(self):
#		return super(MaleManager, self).get_queryset().filter(kelamin='M')
#
#class FemaleManager(models.Manager):
#	def get_queryset(self):
#		return super(FemaleManager, self).get_queryset().filter(kelamin='F')
#
#class Person(models.Model):
#	fname = models.CharField(max_length=20)
#	lname = models.CharField(max_length=20)
#	kelamin = models.CharField(max_length=1, 
#		choices = (
#			('M','Male'),
#			('F','Female')
#			))
#
#	People = models.Manager()
#	men = MaleManager()
#	women = FemaleManager()
#
#	def __str__(self):
#		return '%s %s' %(self.fname, self.lname)
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Publisher)

class AuthorAdmin(admin.ModelAdmin):
	list_display=('f_name', 'l_name')
	search_fields=('f_name', 'l_name')

admin.site.register(Author, AuthorAdmin)

class BooksAdmin(admin.ModelAdmin):
	list_display=('title', 'publisher', 'pub_date')
	list_filter=('pub_date',)
	date_hierarchy='pub_date'
	ordering = ('-pub_date',)
	fields =('title', 'author', 'publisher')
	filter_horizontal = ('author',)
	raw_id_fields = ('publisher',) 

admin.site.register(Books, BooksAdmin)
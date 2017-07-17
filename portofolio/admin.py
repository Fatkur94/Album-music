from django.contrib import admin
from .models import Category, Technology, Post_Portofolio

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class TechnologyAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Technology, TechnologyAdmin)

class Post_PortofolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'description', 'source', 'demo')
	filter_horizontal = ('technology',)


admin.site.register(Post_Portofolio, Post_PortofolioAdmin)
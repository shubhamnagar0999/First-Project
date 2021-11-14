from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from Home.models import Catergory,Post
from django.contrib.admin import ModelAdmin, register


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('cat',)
    list_display = ('title',)
    search_fields = ('title',)



admin.site.register(Catergory,CategoryAdmin)
admin.site.register(Post,PostAdmin)
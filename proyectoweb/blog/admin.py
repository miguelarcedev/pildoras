from django.contrib import admin

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

from .models import Catergoria, Post

admin.site.register(Catergoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
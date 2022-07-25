from django.contrib import admin

# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class ProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

from .models import CategoriaProd, Producto

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProdAdmin)

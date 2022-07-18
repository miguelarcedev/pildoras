from django.contrib import admin

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

from .models import Servicio

admin.site.register(Servicio, ServicioAdmin)
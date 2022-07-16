from django.urls import path
from proyectowebapp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('servicio', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),

]

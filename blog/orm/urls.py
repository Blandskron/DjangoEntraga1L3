from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.crearAutor, name='home'),
    path('articulo/', views.crearArticulo, name='articulo'),
    path('ver_articulos/', views.ver_articulos, name='ver_articulos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
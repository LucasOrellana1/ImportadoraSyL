from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('productos,/', views.productos, name = 'productos'),

    path('producto/<int:id_producto>/', views.producto, name='detalle_producto'),

]

#Permite que se vean las imagenes de la BD:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
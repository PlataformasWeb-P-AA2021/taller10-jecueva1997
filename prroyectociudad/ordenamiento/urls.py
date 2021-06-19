"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('listado-parroquias', views.listadoParroquias, 
            name='listadoParroquias'),
        path('listado-barrios', views.listadoBarrios, 
            name='listadoBarrios'),
        path('crear/parroquia', views.crear_parroquia, 
            name='crear_parroquia'),
        path('editar/parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
        path('editar/barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
        path('crear/barrio/parroquia/<int:id>', 
            views.crear_barrio_parroquia, 
            name='crear_barrio_parroquia'),
 ]

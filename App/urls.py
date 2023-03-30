from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<str:name>/<str:price>/<str:description>/<str:stock>', views.create, name='create'),
    path('datos', views.datos, name='datos'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>/<str:name>/<str:price>/<str:description>/<str:stock>', views.update, name='update'),
    path('ver_producto/<int:id>', views.ver_producto, name='ver'),
    path('formcreate', views.formcreate, name='create'),
    path('formupdate/<int:id>', views.ver_producto_para_editar, name='updateform'),
]

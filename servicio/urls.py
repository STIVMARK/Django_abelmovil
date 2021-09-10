"""
    Urls de la aplicacion servicioTecnico
"""
from django.urls import *
from django.contrib import admin
from servicio import views

urlpatterns = [


    #path('', views.login),

    path('', views.index, name="index"),


    #Rutas usuario
    path('c_usuario/', views.c_usuario, name='c_usuario'),
    path('r_usuario/', views.r_usuario, name='r_usuario'),
    path('u_usuario/<int:id>', views.u_usuario,name='u_usuario'),
    path('d_usuario/<int:id>', views.d_usuario,name='d_usuario'),

    # Rutas cliente
    path('c_cliente/', views.c_cliente, name='c_cliente'),
    path('r_cliente/', views.r_cliente, name='r_cliente'),
    path('u_cliente/<int:id>', views.u_cliente, name='u_cliente'),
    path('d_cliente/<int:id>', views.d_cliente, name='d_cliente'),

    # Rutas cliente
    path('c_cliente/', views.c_cliente, name='c_cliente'),
    path('r_cliente/', views.r_cliente, name='r_cliente'),
    path('u_cliente/<int:id>', views.u_cliente, name='u_cliente'),
    path('d_cliente/<int:id>', views.d_cliente, name='d_cliente'),

    # Rutas mantenimiento
    path('c_mantenimiento/', views.c_mantenimiento, name='c_mantenimiento'),
    path('r_mantenimiento/', views.r_mantenimiento, name='r_mantenimiento'),
    path('u_mantenimiento/<int:id>', views.u_mantenimiento, name='u_mantenimiento'),
    path('d_mantenimiento/<int:id>', views.d_mantenimiento, name='d_mantenimiento'),

    # Rutas nota_venta
    path('c_nota_venta/', views.c_nota_venta, name='c_nota_venta'),
    path('r_nota_venta/', views.r_nota_venta, name='r_nota_venta'),
    path('u_nota_venta/<int:id>', views.u_nota_venta, name='u_nota_venta'),
    path('d_nota_venta/<int:id>', views.d_nota_venta, name='d_nota_venta'),


    # Rutas detalle_nota_venta
    path('c_detalle_nota_venta/', views.c_detalle_nota_venta, name='c_detalle_nota_venta'),
    path('r_detalle_nota_venta/', views.r_detalle_nota_venta, name='r_detalle_nota_venta'),
    path('u_detalle_nota_venta/<int:id>', views.u_detalle_nota_venta, name='u_detalle_nota_venta'),
    path('d_detalle_nota_venta/<int:id>', views.d_detalle_nota_venta, name='d_detalle_nota_venta'),

    # Rutas factura
    path('c_factura/', views.c_factura, name='c_factura'),
    path('r_factura/', views.r_factura, name='r_factura'),
    path('u_factura/<int:id>', views.u_factura, name='u_factura'),
    path('d_factura/<int:id>', views.d_factura, name='d_factura'),
















]

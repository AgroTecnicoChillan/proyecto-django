from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list_view, name='client_list'),
    path('clientes-django/', views.listado_clientes_django, name='listado_clientes_django'),
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),

]
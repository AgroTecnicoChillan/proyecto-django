from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list_view, name='client_list'),
    # Aquí puedes añadir más URLs para crear, editar, borrar clientes más adelante
    # path('clients/new/', views.client_create_view, name='client_create'),
    # path('clients/<int:client_id>/edit/', views.client_update_view, name='client_update'),
    # path('clients/<int:client_id>/delete/', views.client_delete_view, name='client_delete'),
]
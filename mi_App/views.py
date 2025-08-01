from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import requests
from .supabase_utils import get_all_clients, create_client, update_client, delete_client

def index(request):
    return render(request, 'index.html')

def client_list_view(request):
    # ... el resto de tu código para client_list_view
    clients = []
    error_message = None
    try:
        clients = get_all_clients()
    except requests.exceptions.RequestException as e:
        error_message = f"Error al conectar con Supabase: {e}. Revisa tus credenciales y conexión."
    except Exception as e:
        error_message = f"Ocurrió un error inesperado: {e}"

    context = {
        'clients': clients,
        'error_message': error_message,
    }
    return render(request, 'client_list.html', context)
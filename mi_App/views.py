from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import requests
from .models import Cliente
from .supabase_utils import get_all_clients, create_client, update_client, delete_client
from .forms import ClienteForm


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

    # NUEVA VISTA para usar el modelo de Django
def listado_clientes_django(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista_cliente.html', context)

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes_django')
    else:
        form = ClienteForm()

    context = {'form': form}
    return render(request, 'crear_cliente.html', context)
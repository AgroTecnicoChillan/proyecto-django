import requests
import os
from django.conf import settings # Para acceder a las credenciales de settings.py
# Ya no necesitamos estas importaciones si usas 'requests' directamente:
# from supabase import create_client, Client

# Obtener credenciales de Supabase desde settings.py
SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_KEY = settings.SUPABASE_KEY

HEADERS = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation' # Para que las respuestas incluyan los datos modificados
}

BASE_API_URL = f'{SUPABASE_URL}/rest/v1/clients'

def get_all_clients():
    """Obtiene todos los clientes de Supabase."""
    try:
        response = requests.get(BASE_API_URL, headers=HEADERS)
        response.raise_for_status() # Lanza un error si la solicitud no fue exitosa (código 4xx o 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener clientes de Supabase: {e}")
        return [] # Retorna una lista vacía en caso de error

def create_client(data):
    """Crea un nuevo cliente en Supabase."""
    try:
        response = requests.post(BASE_API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json() # Esto debería devolver una lista con el objeto creado
    except requests.exceptions.RequestException as e:
        print(f"Error al crear cliente en Supabase: {e}")
        return None # Retorna None en caso de error

def update_client(client_id, data):
    """Actualiza un cliente existente en Supabase por su ID."""
    try:
        # Se usa 'eq' (equals) para filtrar por ID en la API de Supabase
        response = requests.patch(f'{BASE_API_URL}?id=eq.{client_id}', headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al actualizar cliente en Supabase: {e}")
        return None

def delete_client(client_id):
    """Elimina un cliente de Supabase por su ID."""
    try:
        response = requests.delete(f'{BASE_API_URL}?id=eq.{client_id}', headers=HEADERS)
        response.raise_for_status()
        return response.status_code == 204 # 204 No Content es éxito para DELETE
    except requests.exceptions.RequestException as e:
        print(f"Error al eliminar cliente en Supabase: {e}")
        return False # Retorna False en caso de error
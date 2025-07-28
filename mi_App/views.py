from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#def index(request):
   #return HttpResponse("<h1>¡Hola Mundo!......GRacias GEMINI por su ayuda</h1>")
def index(request):
    return render(request, 'index.html')


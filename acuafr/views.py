from django.shortcuts import render, HttpResponse
import requests



def index(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'latitud' in request.GET:
        pregunta1 = request.GET['pregunta1']
        pregunta2 = request.GET['pregunta2']
        pregunta3 = request.GET['pregunta3']
        latitud = request.GET['latitud']
        altitud = request.GET['altitud']
        # Verifica si el value no esta vacio
        if latitud:
            # Crea el json para realizar la petición POST al Web Service
            args = {'pregunta1': pregunta1, 'pregunta2':pregunta2, 'pregunta3':pregunta3, 'latitud':latitud, 'altitud':altitud}
            #response = requests.post('http://127.0.0.1:8000/formularios/', args)
            response = requests.post('http://pi1-eafit-acua.azurewebsites.net/formularios/', args)
            # Convierte la respuesta en JSON
            acuafrs_json = response.json()
    if 'cupo' in request.GET:
        tipo = request.GET['tipo']
        carac = request.GET['carac']
        direction = request.GET['direction']
        cupo = request.GET['cupo']
        # Verifica si el value no esta vacio
        if cupo:
            # Crea el json para realizar la petición POST al Web Service
            args = {'tipo': tipo, 'carac':carac, 'direction':direction, 'cupo':cupo}
            #response = requests.post('http://127.0.0.1:8000/eventos/', args)
            response = requests.post('http://pi1-eafit-acua.azurewebsites.net/eventos/', args)
            # Convierte la respuesta en JSON
            acuafrs_json = response.json()
    # Realiza una petición GET al Web Services
    #response = requests.get('http://127.0.0.1:8000/formularios/')
    response = requests.get('http://pi1-eafit-acua.azurewebsites.net/formularios/')
    response = requests.get('http://pi1-eafit-acua.azurewebsites.net/eventos/')
    # Convierte la respuesta en JSON
    arboles = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "acuafr/index.html", {'arboles': arboles})

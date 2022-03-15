from django import urls
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients #Importer la classe Clients
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def clients(request):
    if request.method == "POST":
        """ pseudo = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        ... """

        Clients.objects.create(pseudo="Bernard", zipcode=75012)
        return HttpResponse(request.POST['name'])

    data = Clients.objects.all() #Récupère tous les enregistrements du tableau
    clients = []
    for client in data:
        params = {
            'id':int(client.id),
            'pseudo' : str(client.pseudo),
            'email' :str(client.email),
            'zipcode' :int(client.zipcode),
            'bio':str(client.bio), #Transformation de chaque enregistement de type data (données) en type String(chaine de caractères)
            #'password':str(client.password),#
        }
        clients.append(params)
    #Retourne la transformation du dessus en format json sans caractères spéciaux (ensure_ascii) avec une indentation de 2 au lieu de 4(par défaut)
    json_str = json.dumps(clients, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
















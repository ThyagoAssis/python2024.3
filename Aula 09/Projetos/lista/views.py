from django.shortcuts import render

#Importando a classe do HTTPresponse
from django.http import HttpResponse

#Criar uma função com um paramentro par receber a requisição
def home(request):
    #Uando o httpresponse para uma resposta simples
    #return HttpResponse("<h1>Ola Mundo!</h1>")
    return render(request, "minha_lista/minha_lista.html")

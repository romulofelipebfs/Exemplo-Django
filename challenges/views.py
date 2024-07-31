from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.f

mes_desafio = {
    "janeiro":"janeiro",
    "fevereiro":"fevereiro",
    "marco": "março"
}


def index(request): 
    list_items = ""
    meses = list(mes_desafio.keys())
    for mes in meses:
        mes_maiusculo = mes.capitalize()
        mes_path = reverse('desafio_mes', args=[mes])
        list_items += f"<li><a href=\"{mes_path}\">{mes_maiusculo}</a></li>"


    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def mes_numero(request, mes):
    meses = list(mes_desafio.keys())

    if mes > len(meses):
        return HttpResponseNotFound('Mes invalido')

    redirect_mes = meses[mes - 1]
    
    redirect_path = reverse('desafio_mes', args=[redirect_mes]) #/challenges/mes
    
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)

def mes(request, mes):
    try:
        text_mes = mes_desafio[mes]
        response_data = f"<h1>{text_mes}</h1>"
        return HttpResponse(response_data)
    except:
       return HttpResponseNotFound('Could not find')
   
    

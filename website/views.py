from django.shortcuts import render, get_object_or_404
from .models import Ator, App, ConteudoPagina

def index(request):
    context = {
        "elenco": Ator.objects.all(),
        "app": App.objects.first(),
        "conteudo": ConteudoPagina.objects.filter(pagina='inicio').first(),
    }
    return render(request, "website/index.html", context)

def sobre(request):
    context = {
        "app": App.objects.first(),
        "conteudo": ConteudoPagina.objects.filter(pagina='sobre').first(),
    }
    return render(request, "website/sobre.html", context)

def elenco(request):
    context = {
        "elenco": Ator.objects.order_by('-id'),
        "conteudo": ConteudoPagina.objects.filter(pagina='elenco').first(),
        "app": App.objects.first(),
    }
    return render(request, "website/elenco.html", context)


def ator(request, id_ator):
    ator = get_object_or_404(Ator,id=id_ator)
    context = {
        "ator": ator,
        "app": App.objects.first(),
    }
    return render(request, "website/ator.html", context)
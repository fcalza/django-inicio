from django.shortcuts import render

# Create your views here.
# responsavel por gerenciar o que vai pra tela


def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
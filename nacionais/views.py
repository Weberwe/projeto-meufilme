from django.shortcuts import render
from utilidades.opcoes.fabrica import falsos

DADOS = [falsos() for _ in range(50)]
dados = {'todos': DADOS}

# Create your views here.
def v_nacionais(request):
    global dados
    return render(request, 'nacionais/paginas/nacionais.html',context=dados)

def v_nac_acao(request):
    return render(request, 'nacionais/paginas/acao.html', context=dados)

def v_nac_comedia(request):
    return render(request, 'nacionais/paginas/comedia.html', context=dados)

def v_nac_documentario(request):
    return render(request, 'nacionais/paginas/documentario.html', context=dados)

def v_nac_drama(request):
    return render(request, 'nacionais/paginas/drama.html', context=dados)

def v_nac_terror(request):
    return render(request, 'nacionais/paginas/terror.html', context=dados)

def v_nac_detalhamento(request, genero, titulo):
    resultado = {}
    for item in dados['todos']:    
            if item['titulo'] == titulo:
                resultado = item         
                break
            else:
                 resultado = {'msg':'Infelizmente, este filme não está presente em nosso catálogo'}
    return render(request, 'nacionais/paginas/detalhes.html', context= resultado )

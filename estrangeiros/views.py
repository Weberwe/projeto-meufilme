from django.shortcuts import render
from utilidades.opcoes.fabrica import falsos

DADOS = [falsos() for _ in range(50)]
dados = {'todos': DADOS}

# Create your views here.
def v_estrangeiros(request):
    global dados
    return render(request, 'estrangeiros/paginas/estrangeiros.html',context=dados)

def v_est_acao(request):
    return render(request, 'estrangeiros/paginas/acao.html', context=dados)

def v_est_comedia(request):
    return render(request, 'estrangeiros/paginas/comedia.html', context=dados)

def v_est_documentario(request):
    return render(request, 'estrangeiros/paginas/documentario.html', context=dados)

def v_est_drama(request):
    return render(request, 'estrangeiros/paginas/drama.html', context=dados)

def v_est_terror(request):
    return render(request, 'estrangeiros/paginas/terror.html', context=dados)

def v_est_detalhamento(request, genero, titulo):
    resultado = {}
    for item in dados['todos']:
        # if item['origem'] == 'Filme Estrangeiro':
        #     print('\n\n\n',item['titulo'], '\n\n\n',item['origem'], '\n\n\n', titulo)     
            if item['titulo'] == titulo:
                print('oi')
                resultado = item         
                break
    return render(request, 'estrangeiros/paginas/detalhes.html', context= resultado )

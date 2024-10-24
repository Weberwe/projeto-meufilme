from faker import Faker
import random

# especifica o idioma do texto gerado
FAKE = Faker('pt_BR')

# variável global usada para gerar um valor sequencial para as versões

def falsos():
    origem = ['Filme Nacional', 'Filme Estrangeiro']

    generos = ['Ação', 'Comédia', 'Drama', 'Terror', 'Documentário']
    imagens = [
    {'url': f'https://loremflickr.com/310/420/capa?random={i}'}
    for i in range(40)
    ]
    informacoes = {
        'origem': random.choice(origem),
        'titulo': FAKE.word(),
        'genero': random.choice(generos),
        'data': FAKE.date_time().year,
        'diretor': {
            'nome': FAKE.first_name(),
            'sobrenome': FAKE.last_name()},
        'descricao': FAKE.paragraph(nb_sentences=15),
        'imagem': random.choice(imagens),
                
        }
    
    return informacoes

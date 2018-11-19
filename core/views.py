from django.shortcuts import render

from core.models import Curso


# View inicial onde aparecerá o formulário de pesquisa
def home(request):
    return render(request, 'index.html')


# View responsável pela pesquisa padrão dos cursos
def pesquisa(request):
    # Aqui eu pego todos os cursos para começarmos a trabalhar
    cursos = Curso.objects.all()

    # Atribuo a variavel 'curso_pesquisado' o valor pesquisado no formulário que agora está na URL
    # lembrando que 'nomeInstituicao' é o atributo 'name' do input do formulário e que virou
    # o campo na URL
    curso_pesquisado = request.GET.get('nomeInstituicao')

    # Se existir o valor na pesquisa
    if curso_pesquisado is not None:
        # Então filtre os cursos de acordo pelo seu nome
        cursos = cursos.filter(nome__icontains=curso_pesquisado)

    context = {
        'cursos': cursos
    }

    return render(request, 'pesquisa.html', context)
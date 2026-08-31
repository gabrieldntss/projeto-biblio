from django.shortcuts import render, get_object_or_404
from .models import acervo, autor


def lista_livros(request):
    livros = acervo.objects.all()
    return render(request, 'acervo/lista_livros.html', {'livros': livros})


def detalhe_livro(request, pk):
    livro = get_object_or_404(acervo, pk=pk)
    return render(request, 'acervo/detalhe_livro.html', {'livro': livro})


def lista_autores(request):
    autores = autor.objects.all()
    return render(request, 'acervo/lista_autores.html', {'autores': autores})


def detalhe_autor(request, pk):
    autor_obj = get_object_or_404(autor, pk=pk)
    return render(request, 'acervo/detalhe_autor.html', {'autor': autor_obj})

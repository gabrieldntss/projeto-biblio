from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/<int:pk>/', views.detalhe_autor, name='detalhe_autor'),
]

from django.urls import path, include
from core import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.UploadArquivoView.as_view(), name='upload'),
    path('arquivos/', views.arquivo_lista_last, name='arquivo_lista_last'),
    path('arquivos/all', views.ArquivoListView.as_view(), name='arquivo_lista'),
    path('arquivos/<int:pk>/', views.delete_arquivo, name='delete_arquivo'),
    path('livros/', views.livro_lista, name='livro_lista'),
    path('livros/upload/', views.upload_livro, name='upload_livro'),
    path('livros/<int:pk>/', views.delete_livro, name='delete_livro'),
    path('class/livros/', views.LivroListView.as_view(), name='class_livro_lista'),
    path('class/livros/upload/', views.UploadLivroView.as_view(), name='class_upload_livro'),
]

from django.urls import path, include
from core import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.upload, name='upload'),
    path('livros/', views.livro_lista, name='livro_lista'),
    path('livros/upload/', views.upload_livro, name='upload_livro'),
]

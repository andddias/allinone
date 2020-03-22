from django.db import models


# Exemplo de Model gravando no banco de dados link do arquivo permitira CRUD
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='livros/pdfs/')

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo

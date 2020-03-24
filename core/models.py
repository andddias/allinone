from django.db import models


class Arquivo(models.Model):
    data_upload = models.DateField('Data Upload', auto_now_add=True)
    arquivo = models.FileField(upload_to='arquivos/')

    def __str__(self):
        return str(self.arquivo)


# Exemplo de Model gravando no banco de dados link do arquivo permitira CRUD
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='livros/pdfs/')
    capa = models.ImageField(upload_to='livros/capas/', null=True, blank=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.capa.delete()
        super().delete(*args, **kwargs)

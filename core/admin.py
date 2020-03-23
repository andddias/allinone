from django.contrib import admin

from .models import Arquivo, DataUpload


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'arquivos', 'data_upload')


@admin.register(DataUpload)
class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_upload')

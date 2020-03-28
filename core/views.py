from allinone.settings import BASE_DIR
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LivroForm, ArquivoForm
from .models import Livro, Arquivo

from .cnab_bradesco import lista_dados, tabela_dados_csv, filtra_geracao_cnab


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['arquivo']
        # instanciando FileSystemStorage
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file.name)
    return render(request, 'upload.html', context)


def livro_lista(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'livro_lista.html', context)


def upload_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('livro_lista')
    else:
        form = LivroForm()
    context = {
        'form': form,
    }
    return render(request, 'upload_livro.html', context)


def delete_livro(request, pk):
    if request.method == 'POST':
        livro = Livro.objects.get(pk=pk)
        livro.delete()
    return redirect('livro_lista')


class LivroListView(ListView):
    model = Livro
    template_name = 'class_livro_lista.html'
    context_object_name = 'livros'


class UploadLivroView(CreateView):
    model = Livro
    template_name = 'upload_livro.html'

    # forma correta
    form_class = LivroForm
    # ou
    # fields = ('titulo', 'autor', 'pdf', 'capa')

    success_url = reverse_lazy('class_livro_lista')


class UploadArquivoView(LoginRequiredMixin, CreateView):
    template_name = 'upload.html'
    form_class = ArquivoForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        arquivos = request.FILES.getlist('arquivo')
        if form.is_valid():
            for arq in arquivos:
                arquivo_instancia = Arquivo(arquivo=arq)
                arquivo_instancia.save()
            messages.success(self.request, message='Upload feito com sucesso!')
            return HttpResponseRedirect('/arquivos/')
        else:
            return self.form_invalid(form)


class ArquivoListView(LoginRequiredMixin, ListView):
    model = Arquivo
    template_name = 'arquivo_lista.html'
    context_object_name = 'arquivos'


@login_required
def arquivo_lista_last(request):
    try:
        data = Arquivo.objects.last().data_upload
        arquivos = Arquivo.objects.filter(data_upload=data)
    except AttributeError:
        arquivos = None
    context = {
        'arquivos': arquivos,
        'row1': 'row1',
        'row2': 'row2',
    }
    return render(request, 'arquivo_lista_last.html', context)


def update_variable(value):
    if value:
        value = False
        return value
    else:
        value = True
        return value


@login_required
def processamento_arquivo(request):
    data = Arquivo.objects.last().data_upload
    arquivos = Arquivo.objects.filter(data_upload=data)

    endereco_arq = []
    for arq in arquivos:
        endereco_arq.append(BASE_DIR + arq.arquivo.url)

    lista = lista_dados(endereco_arq)
    tabela_csv = tabela_dados_csv(lista)
    lista_arq_cnab = filtra_geracao_cnab()

    context = {
        'tabela_csv': tabela_csv,
        'lista_cnab': lista_arq_cnab,
    }
    return render(request, 'arquivo_resultado.html', context)


@login_required
def delete_arquivo(request, pk):
    if request.method == 'POST':
        arquivo = Arquivo.objects.get(pk=pk)
        arquivo.delete()
    return redirect('arquivo_lista_last')

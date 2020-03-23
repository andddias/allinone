from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LivroForm, ArquivoForm
from .models import Livro, Arquivo, DataUpload

from .cnab_bradesco import lista_dados


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
        arquivos = request.FILES.getlist('arquivos')
        if form.is_valid():
            data_upload_instancia = DataUpload()
            data_upload_instancia.save()
            for arq in arquivos:
                arquivo_instancia = Arquivo(data_upload=data_upload_instancia, arquivos=arq)
                arquivo_instancia.save()
            messages.success(self.request, message='Upload feito com sucesso!')
            return HttpResponseRedirect('/upload/')
        else:
            return self.form_invalid(form)

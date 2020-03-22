from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LivroForm
from .models import Livro

from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

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

"""
class MyModelView(FormView):
    form_class = MyModelForm
    template_name = 'upload.html'
    #login_url = '/accounts/login/'
    success_url = '/upload/'
    #success_message = 'Upload feito com sucesso!'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print(f)
            # dados = lista_dados(files)
            print(type(files))
            print(files)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FileFildView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'
    login_url = '/accounts/login/'
    success_url = '/upload/'
    success_message = 'Upload feito com sucesso!'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print(type(f))
            # dados = lista_dados(files)
            print(type(files))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import FileFieldForm, MyModelForm
from .models import MyModel
from .cnab_bradesco import lista_dados


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')




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

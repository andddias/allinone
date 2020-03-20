from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import FileFieldForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'


class FileFildView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'
    login_url = '/accounts/login/'
    success_url = '/success/'
    success_message = 'Upload feito com sucesso!'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

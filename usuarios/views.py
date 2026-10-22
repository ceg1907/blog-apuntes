from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from posts.models import Post
from .forms import RegistroForm, PerfilForm


class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        respuesta = super().form_valid(form)
        login(self.request, self.object)
        return respuesta


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mis_posts'] = Post.objects.filter(autor=self.request.user)
        return context


class EditarPerfilView(LoginRequiredMixin, UpdateView):
    form_class = PerfilForm
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user

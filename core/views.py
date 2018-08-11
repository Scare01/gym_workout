from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


from django.urls import reverse_lazy
from core.models import ProgramForm, Program, ExcercisesForm


class IndexPageView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Program.objects.all()


class ProgramDetailView(DetailView):
    template_name = 'programdetail.html'
    model = Program

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Program.objects.filter(pk=self.kwargs.get('pk'))
        return context


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class AddProgramView(FormView):
    form_class = ProgramForm
    success_url = reverse_lazy('index')
    template_name = 'addprogram.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateExerciseView(FormView):
    form_class = ExcercisesForm
    success_url = reverse_lazy('index')
    template_name = 'createexcercise.html'

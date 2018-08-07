from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexPageView(TemplateView):
    template_name = 'index.html'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import AdvUserCreationForm, MainForm, UserPasswordChangeForm
from .models import *


def index(request):
    if str(request.user) == "AnonymousUser":
        return render(request, 'index.html')
    else:
        mails = Mail.objects.filter(recipient=request.user)
        mails_count = Mail.objects.filter(recipient=request.user).count()
        return render(request, 'index.html', {'mails': mails, 'mails_count': mails_count})


def mail_detail(request, pk):
    mail = Mail.objects.get(pk=pk)
    print(mail)
    return render(request, 'detail.html', {'mail': mail})


def mail_add(request):
    if request.method == "POST":
        form = MainForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sender = request.user
            instance.save()
            return redirect('main')
    else:
        users = dict(map(lambda user: (user.id, user.username), AdvUser.objects.all()))
    return render(request, 'mail_add.html', {"users": users})


class RegistrationFormView(CreateView):
    model = AdvUser
    form_class = AdvUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('main')

    def post(self, request, *args, **kwargs):
        form = AdvUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dolzns'] = dict(map(lambda dolzn: (dolzn.id, dolzn.name), Dolzn.objects.all()))
        return context


class MainLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url


def log_out(request):
    logout(request)
    return render(request, 'index.html')


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Изменение пароля пользователя
    """
    form_class = UserPasswordChangeForm
    template_name = 'password_change.html'
    success_message = 'Ваш пароль был успешно изменён!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        return context

    def get_success_url(self):
        return reverse_lazy('main')

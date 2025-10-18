from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from users.forms import UserRegisterForm


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, email):
        subject = 'Добро пожаловать на сайт'
        message = 'Спасибо что зарегистрировались на нашем сайте'
        from_email = 'user_address@mail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('mailing:mailing_list')
    fields = ('username', 'password')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('mailing:mailing_list')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Получаем email из формы
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)  # Авторизуем пользователя
                return redirect('home')  # Перенаправляем на главную страницу
            else:
                form.add_error(None, "Неверный email или пароль.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
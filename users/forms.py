from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser
from django import forms
from django.contrib.auth import authenticate


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', ]


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        template_name = 'registration/login.html'

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", max_length=254)  # Используем email вместо username
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Неверный email или пароль.")
            if not user.is_active:
                raise forms.ValidationError("Этот аккаунт отключен.")
        return self.cleaned_data
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, User
from django.core.validators import validate_email

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(label='Эл. Почта', widget=forms.TextInput(attrs={'class': 'my-input-class'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'my-input-class'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'my-input-class'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'my-input-class'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'my-input-class'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            try:
                validate_email(email)
            except forms.ValidationError:
                raise forms.ValidationError("Некорректный email-адрес")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            if len(password1) < 8:
                raise forms.ValidationError("Пароль должен содержать не менее 8 символов")
            elif password1.isalpha() or password1.isdigit():
                raise forms.ValidationError("Пароль должен содержать как минимум одну букву и одну цифру")
            elif len(password1) > 30:
                raise forms.ValidationError("Значение пароля должно содержать не более 30 символов")
        return password1
    def clean_password2(self):
        password2 = self.cleaned_data.get('password1')
        if password2:
            if len(password2) < 8:
                raise forms.ValidationError("Пароль должен содержать не менее 8 символов")
            elif password2.isalpha() or password2.isdigit():
                raise forms.ValidationError("Пароль должен содержать как минимум одну букву и одну цифру")
            elif len(password2) > 30:
                raise forms.ValidationError("Значение пароля должно содержать не более 30 символов")
        return password2

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            if len(first_name) < 2:
                raise forms.ValidationError("Имя должно содержать не менее 2 символов")
            elif not first_name.isalpha():
                raise forms.ValidationError("Имя может содержать только буквы")
            elif len(first_name) > 30:
                raise forms.ValidationError("Значение имени должно содержать не более 30 символов")
        return first_name



    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            if len(last_name) < 2:
                raise forms.ValidationError("Фамилия должна содержать не менее 2 символов")
            elif not last_name.isalpha():
                raise forms.ValidationError("Фамилия может содержать только буквы")
            elif len(last_name) > 30:
                raise forms.ValidationError("Значение фамилии должно содержать не более 30 символов")
        return last_name

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


# reg

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        help_text='Номер телефона. Формат +7910...', label='test'
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Одна большая буква и т.д.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )



from django import forms
from .models import Profile
from django.forms.widgets import FileInput


class CustomFileInput(FileInput):
    def render_file_input(self, name, value, attrs=None, renderer=None):
        html = super().render_file_input(name, value, attrs, renderer)
        html = html.replace('Файл не выбран', '')  # заменяем текст на пустую строку
        return html

class ProfileForm(forms.ModelForm):
    pic = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': ' '}), label_suffix='')

    class Meta:
        model = Profile
        fields = ['pic']
from django import forms

class UserRegisterForm(forms.Form):
    login = forms.CharField(max_length=30,
                            label="Введите логин: ")
    password = forms.CharField(widget=forms.PasswordInput(),
                               min_length=8,
                               label='Введите пароль:')
    repeat_password = forms.CharField(widget=forms.PasswordInput(),
                                      min_length=8,
                                      label='Повторите пароль:')
    age = forms.CharField(widget=forms.NumberInput(),
                          max_length=3,
                          label="Введите возраст: ")
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegisterForm

users = [['user1',
          '12345678',
          '18'],
         ['UltraSobaka',
          'qwertyui',
          '44'],
         ['MegaSobaka',
          'asdfdhjkl',
          '34']]

info = dict()

def check_user(login,
               password,
               repeat_password,
               age):
    if password != repeat_password:
        info['error'] = "Неверный пароль!"
        print(info)
        return HttpResponse(info['error'])
    elif int(age) < 18:
        info['error'] = "Вы должны быть старше 18!"
        print(info)
        return HttpResponse(info['error'])
    elif any(e[0] == login for e in users):
        info['error'] = "Такой пользователь уже существует!"
        print(info)
        return HttpResponse(info['error'])
    else:
        info['hello'] = f"Приветствуем, {login}!"
        print(info)
        return HttpResponse(info['hello'])


def sign_up_by_html(request):
    info.clear()

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        check_user(login,
                   password,
                   repeat_password,
                   age)

    context = {
        'info': info,
    }
    print(context)

    return render(request,
                  'fifth_task/registration_page.html',
                  context=context)


def sign_up_by_django(request):
    info.clear()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            check_user(login,
                       password,
                       repeat_password,
                       age)

    else:
        form = UserRegisterForm()

    context = {
        'info': info,
        'form': form
    }
    print(context)

    return render(request,
                  'fifth_task/registration_page.html',
                  context=context)

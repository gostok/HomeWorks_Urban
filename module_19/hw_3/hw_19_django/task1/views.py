from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .forms import UserRegister
from .models import *


def home(request):
    title = 'Игровая платформа'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'home.html', context)

def game(request):
    games = Game.objects.all()
    text = 'Игры'
    context = {
        'text': text,
        'games': games
    }
    return render(request, 'game.html', context)

def basket(request):
    title = 'Игровая платформа'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'basket.html', context)







def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                if Buyer.objects.filter(name=username).exists():
                    info['error'] = 'Пользователь уже существует'
                else:
                    new_buyer = Buyer(
                        name=username,
                        password=make_password(password),
                        age=age
                    )
                    new_buyer.save()
                    info['welcome_message'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                if Buyer.objects.filter(name=username).exists():
                    info['error'] = 'Пользователь уже существует'
                else:
                    new_buyer = Buyer(
                        name=username,
                        password=make_password(password),
                        age=age
                    )
                    new_buyer.save()
                    info['welcome_message'] = f'Приветствуем, {username}!'

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    title = 'Игровая платформа'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'home.html', context)

def game(request):
    title = 'Игровая платформа'
    text = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Mario']
    context = {
        'title': title,
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

from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'fourth_task/main.html'

class ShopView(TemplateView):
    template_name = 'fourth_task/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = [('Атомное сердце', 1000),
                 ('Механизированный оторва из будущего', 2000),
                 ('Плати день', 500)]
        context['games'] = games
        return context

class CartView(TemplateView):
    template_name = 'fourth_task/cart.html'
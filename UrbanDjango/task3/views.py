from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'third_task/main.html'

class ShopView(TemplateView):
    template_name = 'third_task/shop.html'

class CartView(TemplateView):
    template_name = 'third_task/cart.html'

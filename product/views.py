from django.views.generic import TemplateView
from django.shortcuts import render
from product.models import Product, UnitMeasure, Category, Brand, Images
from django.urls import reverse

# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = 'Sujan Shah'
        context['product_list'] = Product.objects.all()
        return context

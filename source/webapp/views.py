from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'

class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'image')
    success_url = reverse_lazy('webapp:index')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product/update.html'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')

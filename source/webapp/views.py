from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ProductReviewForm, ReviewForm
from webapp.models import Product, Review


class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'

class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'

class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'image')
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.add_product'
    permission_denied_message = 'Доступ ограничен'

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product/update.html'
    permission_required = 'webapp.change_product'
    permission_denied_message = 'Доступ ограничен'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
    permission_denied_message = 'Доступ ограничен'

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm

    def get_product(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = self.get_product()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'review/update.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.change_review'
    permission_denied_message = 'Доступ ограничен'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'review/delete.html'
    context_object_name = 'review'
    model = Review
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_review'
    permission_denied_message = 'Доступ ограничен'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']





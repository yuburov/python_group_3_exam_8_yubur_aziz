from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['']

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'mark']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['author', 'product']
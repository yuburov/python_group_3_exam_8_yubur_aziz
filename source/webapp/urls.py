from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreateView,ProductUpdateView, ProductDeleteView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/add-review/', ReviewCreateView.as_view(), name='add_review'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete')
]

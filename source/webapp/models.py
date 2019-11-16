from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('electronics', 'Электроника'),
)

MARK_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='product_images', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey('webapp.Product', related_name='reviews', on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(max_length=3000, verbose_name='Текст отзыва')
    mark = models.IntegerField(null=False, blank=False, choices=MARK_CHOICES, verbose_name='Оценка')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


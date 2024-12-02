from django.db import models
from django.contrib.auth.models import User


def create_path_to_upload(instance: 'Recipe', name: str) -> str:
    folder_name = instance.category.name.replace(' ', '_')
    return f'{folder_name}/{name}'


class Recipe(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True, verbose_name='Название блюда')
    description = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Описание блюда')
    steps = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Шаги приготовления блюда')
    time = models.CharField(max_length=60, blank=False, null=False, verbose_name='Время приготовления блюда')
    image = models.ImageField(upload_to=create_path_to_upload, blank=False, null=False,
                              verbose_name='Изображение блюда')
    author = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=1, related_name='recipes',
                               related_query_name='recipe')
    ingredients = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Ингридиенты')
    category = models.ForeignKey(to='Category', on_delete=models.SET_NULL, null=True, related_name='recipes',
                                 related_query_name='recipe')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    def get_short_description(self):
        if len(self.description) < 40:
            return self.description
        return f'{self.description[:40]}...'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True, verbose_name='Название категории')
    description = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

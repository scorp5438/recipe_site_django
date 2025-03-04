from django.contrib.auth.models import User
from django.db import models


def create_path_to_upload(instance: 'Recipe', name: str) -> str:
    """
    Генерирует путь для загрузки изображения рецепта.

    Args:
        instance (Recipe): Экземпляр модели Recipe, для которого загружается изображение.
        name (str): Имя файла изображения.

    Returns:
        str: Путь для сохранения изображения в формате `{category_name}/{file_name}`.
             Пробелы в названии категории заменяются на подчеркивания.
    """
    folder_name = instance.category.name.replace(' ', '_')
    return f'{folder_name}/{name}'


class Recipe(models.Model):
    """
    Модель, представляющая рецепт.

    Attributes:
        name (CharField): Название блюда. Максимальная длина — 150 символов.
        description (TextField): Описание блюда. Максимальная длина — 2000 символов.
        steps (TextField): Шаги приготовления блюда. Максимальная длина — 5000 символов.
        time (CharField): Время приготовления блюда. Максимальная длина — 60 символов.
        image (ImageField): Изображение блюда. Загружается в папку, сгенерированную функцией `create_path_to_upload`.
        author (ForeignKey): Ссылка на пользователя, создавшего рецепт. По умолчанию — пользователь с id=1.
        ingredients (TextField): Ингредиенты блюда. Максимальная длина — 2000 символов.
        category (ForeignKey): Ссылка на категорию рецепта. Может быть null.
        date_create (DateField): Дата создания рецепта. Заполняется автоматически при создании.

    Methods:
        __str__: Возвращает название рецепта.
        get_short_description: Возвращает сокращенное описание рецепта (первые 40 символов).

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
    """
    name = models.CharField(max_length=150, blank=False, null=False, unique=True, verbose_name='Название блюда')
    description = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Описание блюда')
    steps = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Шаги приготовления блюда')
    time = models.CharField(max_length=60, blank=False, null=False, verbose_name='Время приготовления блюда')
    image = models.ImageField(
        upload_to=create_path_to_upload,
        blank=False, null=False,
        verbose_name='Изображение блюда'
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='recipes',
        related_query_name='recipe'
    )
    ingredients = models.TextField(max_length=2000, blank=False, null=False, verbose_name='Ингридиенты')
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='recipes',
        related_query_name='recipe'
    )
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    def get_short_description(self):
        """
        Возвращает сокращенное описание рецепта.

        Если описание длиннее 40 символов, возвращает первые 40 символов с многоточием.
        Иначе возвращает полное описание.

        Returns:
            str: Сокращенное или полное описание рецепта.
        """
        if len(self.description) < 40:
            return self.description
        return f'{self.description[:40]}...'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Category(models.Model):
    """
    Модель, представляющая категорию рецептов.

    Attributes:
        name (CharField): Название категории. Максимальная длина — 150 символов. Уникальное.
        description (TextField): Описание категории. Максимальная длина — 1000 символов.

    Methods:
        __str__: Возвращает название категории.

    Meta:
        verbose_name (str): Человекочитаемое имя модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
    """
    name = models.CharField(max_length=150, blank=False, null=False, unique=True, verbose_name='Название категории')
    description = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

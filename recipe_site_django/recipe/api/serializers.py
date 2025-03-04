from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..models import Recipe


class RecipeSerializer(ModelSerializer):
    """
    Сериализатор для модели Recipe.

    Поля:
    - id Уникальный идентификатор рецепта
    - name Наименование рецепта
    - description Описание рецепта
    - steps Шаги выполнения
    - time Время рецепта
    - image изображение рецепта
    - ingredients Необходимые ингредиенты
    - date_create Дата создания рецепта
    - author Автор
    - category Категория рецепта

    Используется для:
    - Сериализации данных рецепта при чтении (GET-запросы).
    - Десериализации данных рецепта при создании (POST-запросы).
    """

    author_full_name = SerializerMethodField()
    category_name = SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'steps',
            'time',
            'image',
            'author',
            'author_full_name',
            'ingredients',
            'category',
            'category_name',
            'date_create'
        )

    def get_author_full_name(self, obj):
        if obj.author:
            return obj.author.username

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.name


class RecipeUpdateSerializer(RecipeSerializer):
    """
    Сериализатор для обновления рецепта

    поля:
    - name Наименование блюда
    - description Описание блюда
    - steps Шаги пригтовления
    - time Время приготовления
    - ingredients Ингридиенты
    - category Категория блюда

    используется для
    Десериализации данных при изменении рецепта (PATCH-запрос)
    """
    author_full_name = SerializerMethodField()

    class Meta(RecipeSerializer.Meta):
        fields = (
            'name',
            'description',
            'steps',
            'time',
            'ingredients',
            'category',
            'category_name',
            'author_full_name'
        )

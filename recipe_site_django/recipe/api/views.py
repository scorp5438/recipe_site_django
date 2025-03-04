from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrSuperUser
from .serializers import RecipeSerializer, RecipeUpdateSerializer
from ..models import Recipe


class RecipeApiView(ModelViewSet):
    """
    Представление для работы с рецептами (CRUD операции).

    Поддерживает следующие HTTP-методы:
    - GET: Получение списка рецептов или деталей конкретного рецепта.
    - POST: Создание нового рецепта.
    - PATCH: Частичное обновление существующего рецепта.

    Attributes:
        serializer_class (Serializer): Сериализатор по умолчанию для GET и POST запросов.
        queryset (QuerySet): Набор данных, используемый для получения рецептов.
                             Включает связанные объекты категорий.
        http_method_names (list): Список разрешенных HTTP-методов.

    Methods:
        get_serializer_class: Возвращает сериализатор в зависимости от HTTP-метода.
        get_permissions: Возвращает список разрешений в зависимости от HTTP-метода.
        update: Обрабатывает PATCH-запрос для частичного обновления рецепта.
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.select_related('category').all().order_by('pk')
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.request.method in ['GET', 'POST']:
            return RecipeSerializer
        elif self.request.method == 'PATCH':
            return RecipeUpdateSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [IsAuthenticated()]
        elif self.request.method == 'PATCH':
            return [IsAuthenticated(), IsAuthorOrSuperUser()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        update_serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        if update_serializer.is_valid():
            update_serializer.save()
            return Response({'message': 'Update successfully'})
        return Response(update_serializer.errors, status=400)

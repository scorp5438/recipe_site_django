from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe.api.views import RecipeApiView

app_name = 'api_recipe'

router = DefaultRouter()
router.register(r'v1/recipe', RecipeApiView, basename='recipe')

urlpatterns = [
    path('', include(router.urls))
]



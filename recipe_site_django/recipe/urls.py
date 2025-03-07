from django.urls import path

from .views import RecipeView, CreateRecipeView, DetailRecipeView, UpdateRecipeView

app_name = 'recipe'

urlpatterns = [
    path('', RecipeView.as_view(), name='recipe'),
    path('create_recipe/', CreateRecipeView.as_view(), name='create_recipe'),
    path('detail_recipe/<int:pk>/', DetailRecipeView.as_view(), name='detail_recipe'),
    path('update_recipe/<int:pk>/', UpdateRecipeView.as_view(), name='update_recipe'),
]

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from .models import Recipe, Category


class RecipeView(ListView):
    queryset = Recipe.objects.order_by('?').select_related('category')[:1]
    template_name = 'recipe/index.html'


class DetailRecipeView(DetailView):
    template_name = 'recipe/detail_recipe.html'
    queryset = Recipe.objects.select_related('category')


# TODO потом надо выпилить
class CreateCategoryView(CreateView):
    model = Category
    template_name = 'recipe/create_category.html'
    fields = '__all__'
    success_url = reverse_lazy('recipe:recipe')


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'recipe/create_recipe.html'
    fields = '__all__'
    success_url = reverse_lazy('recipe:recipe')


class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'recipe/update_recipe.html'
    fields = 'name', 'description', 'steps', 'time', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:recipe')

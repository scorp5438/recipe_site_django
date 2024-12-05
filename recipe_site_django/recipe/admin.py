from django.contrib import admin

from .models import Category, Recipe
from django.contrib.auth.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
    search_fields = 'name',


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'short_description', 'short_steps', 'time', 'author_name', 'short_ingredients', 'category', 'date_create'
    list_display_links = 'pk', 'name'
    ordering = 'pk',

    def short_steps(self, obj: Recipe):
        return obj.steps[0:10] + '...'

    short_steps.short_description = 'short steps'

    def short_description(self, obj: Recipe):
        return f'{obj.description[0:10]}...'

    short_description.short_description = 'short description'

    def author_name(self, obj: Recipe):
        return obj.author.first_name or obj.author

    author_name.short_description = 'author name'

    def short_ingredients(self, obj: Recipe):
        return f'{obj.description[0:10]}...'

    short_ingredients.short_description = 'short ingredients'

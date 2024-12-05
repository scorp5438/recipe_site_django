from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy
from .models import Recipe, Category


class RecipeView(ListView):
    queryset = Recipe.objects.order_by('?').select_related('category')[:5]
    template_name = 'recipe/index.html'


class DetailRecipeView(DetailView):
    template_name = 'recipe/detail_recipe.html'
    queryset = Recipe.objects.select_related('category')


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe/create_recipe.html'
    fields = 'name', 'description', 'steps', 'time', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:recipe')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'recipe/update_recipe.html'
    fields = 'name', 'description', 'steps', 'time', 'image', 'ingredients', 'category'
    success_url = reverse_lazy('recipe:recipe')

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        created_by_current_user = self.get_object().author == self.request.user
        return created_by_current_user

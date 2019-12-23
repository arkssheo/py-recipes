from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Recipe
from .forms import RecipeForm

# Create your views here.
# def index(request):
# 	recipes = Recipe.objects.all()
# 	context = {'recipes': recipes}
# 	return render(request, 'recipes/index.html', context)
class RecipeList(ListView):
	model = Recipe

class RecipeDetail(DetailView):
	model = Recipe

class RecipeCreate(CreateView):
	model = Recipe
	fields = ['title', 'submitted_by', 'process']

	def get_success_url(self):
		return reverse('recipes:index')

class RecipeUpdate(UpdateView):
	model = Recipe
	fields = ['title', 'submitted_by', 'process']

	def get_success_url(self):
		return reverse_lazy('recipes:index')

class RecipeDelete(DeleteView):
	model = Recipe

	def get_success_url(self):
		return reverse_lazy('recipes:index')

# def detail(request, recipe_id):
# 	recipe = get_object_or_404(Recipe, pk=recipe_id)
# 	context = {'recipe': recipe}
# 	return render(request, 'recipes/detail.html', context)

# def new(request):
# 	if request.method == 'POST':
# 		form = RecipeForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect("/recipes/")
# 	else:
# 		form = RecipeForm()
# 	return render(request, 'recipes/new.html', { 'form': form })


# def edit(request, recipe_id):
# 	return HttpResponse(f"You're editing recipe {recipe_id}")

# def create(request):
# 	return HttpResponse("OK!")
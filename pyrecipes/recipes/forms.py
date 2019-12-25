from django.forms import ModelForm, Textarea
from .models import Recipe

class RecipeForm(ModelForm):
	class Meta:
		model = Recipe
		fields = ['title', 'submitted_by', 'ingredient_text', 'process']
		widgets = {
			'ingredient_text': Textarea(attrs={'class': 'size-mid'}),
			'process': Textarea(attrs={'class': 'size-lg'}),
		}
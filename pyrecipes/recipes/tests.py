from django.test import TestCase

from .models import Recipe

# Create your tests here.
class RecipeModelTests(TestCase):
	
	def can_create_recipe_defaults(self):
		r = Recipe(title='test recipe')
		self.assertIs(r.title, 'test recipe')
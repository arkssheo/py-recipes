from django.db import models

# Create your models here.
class Recipe(models.Model):
	title = models.CharField(max_length=100)
	submitted_by = models.CharField(max_length=200)
	process = models.TextField('step-by-Step process', max_length=9000)

	def __str__(self):
		return f"'{self.title}', by {self.submitted_by}"

class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	quantity = models.IntegerField(default=0)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.quantity} units of {self.name}(s)"

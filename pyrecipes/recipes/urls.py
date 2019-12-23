from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
	path('', views.RecipeList.as_view(), name='index'),
	path('new/', views.RecipeCreate.as_view(), name='new'),
	path('<int:pk>/', views.RecipeDetail.as_view(), name='detail'),
	path('<int:pk>/edit/', views.RecipeUpdate.as_view(), name='edit'),
	path('<int:pk>/delete/', views.RecipeDelete.as_view(), name='delete'),
]
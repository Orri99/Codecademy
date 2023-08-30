from django.urls import path
from . import views

urlpatterns = [
  path("", views.menu, name="menu"),
  path("ingr/", views.ingr, name="ingr"),
  path("recipe/", views.recipe, name="recipe"),
  path("purch/", views.purch, name="purch"),
  path("ingr/create",views.IngredientCreate.as_view(),name="ingredientcreate"),
  path("ingr/update/<pk>",views.IngredientUpdate.as_view(),name="ingredientupdate"),
  path("ingr/delete/<pk>",views.IngredientDelete.as_view(),name="ingredientdelete")
]
from django.urls import path
from . import views

urlpatterns = [
  path("", views.menu, name="menu"),
  path("menutable/", views.menutable, name="menutable"),
  path("ingr/", views.ingr, name="ingr"),
  path("recipe/", views.recipe, name="recipe"),
  path("purch/", views.purch, name="purch"),
  path("purchasesuccess/",views.purchasesuccess, name = "purchasesuccess"),
  path("purchasefailure/",views.purchasefailure, name = "purchasefailure"),
  path("menuitem/create",views.MenuItemCreate.as_view(),name="menuitemcreate"),
  path("menuitem/update/<pk>",views.MenuItemUpdate.as_view(),name="menuitemupdate"),
  path("menuitem/delete/<pk>",views.MenuItemDelete.as_view(),name="menuitemdelete"),
  path("ingr/create",views.IngredientCreate.as_view(),name="ingredientcreate"),
  path("ingr/update/<pk>",views.IngredientUpdate.as_view(),name="ingredientupdate"),
  path("ingr/delete/<pk>",views.IngredientDelete.as_view(),name="ingredientdelete"),
  path("recipe/create",views.RecipeCreate.as_view(),name="recipecreate"),
  path("recipe/update/<pk>",views.RecipeUpdate.as_view(),name="recipeupdate"),
  path("recipe/delete/<pk>",views.RecipeDelete.as_view(),name="recipedelete"),
  path("purchaseitem/<pk>",views.PurchaseItem.as_view(),name="purchaseitem"),
]
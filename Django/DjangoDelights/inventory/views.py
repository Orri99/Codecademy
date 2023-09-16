from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemCreateForm, MenuItemUpdateForm, IngredientCreateForm, IngredientUpdateForm, RecipeReqCreateForm, RecipeReqUpdateForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def menu(request):
    menu = MenuItem.objects.all()
    context = {"menuitems" : menu }
    return render(request, "inventory/menu.html", context)

def menutable(request):
    menu = MenuItem.objects.all()
    context = {"menuitems" : menu }
    return render(request, "inventory/menutable.html", context)

def ingr(request):
  all_ingredients = Ingredient.objects.all()
  context = {"ingredients" : all_ingredients}
  return render(request, 'inventory/ingr.html', context)

def recipe(request):
    recreqs = RecipeRequirement.objects.all()
    context = {"recreq" : recreqs}
    return render(request, "inventory/recipe.html", context)

def purch(request):
    purchases = Purchase.objects.all()
    context = {"purchases" : purchases}
    return render(request, "inventory/purch.html", context)

def purchasesuccess(request):
    return render(request, "inventory/purchasesuccess.html")

def purchasefailure(request):
    return render(request, "inventory/purchasefailure.html")

class PurchaseItem(TemplateView):
   template_name = "inventory/purchaseitem.html"

   def get_context_data(self, **kwargs):
      menuitem = MenuItem.objects.get(id=kwargs['pk'])
      context = {"menuitem" : menuitem}
      return context

   def post(self, request, **kwargs):
      menuitem = MenuItem.objects.get(id=kwargs['pk'])
      requiredIngredients = menuitem.reciperequirement_set
      ingredientsInStock = True
      for requirement in requiredIngredients.all():
         if requirement.quantity > requirement.ingredient.ingredientStock:
            ingredientsInStock = False
      if ingredientsInStock:
         for requirement in requiredIngredients.all():
            req_ingredient = requirement.ingredient
            req_ingredient.ingredientStock -= requirement.quantity
            req_ingredient.save()
         purchase = Purchase(menu_item=menuitem)
         purchase.save()
         return redirect("/purchasesuccess") 
      else:
         return redirect("/purchasefailure")

class MenuItemCreate(CreateView):
  model = MenuItem
  form_class = MenuItemCreateForm
  template_name = "inventory/menuitem_create_form.html"

class MenuItemUpdate(UpdateView):
   model = MenuItem
   template_name = "inventory/menuitem_update_form.html"
   form_class = MenuItemUpdateForm

class MenuItemDelete(DeleteView):
   model = MenuItem
   template_name = "inventory/menuitem_delete_form.html"
   success_url = "/"

class IngredientCreate(CreateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/ingr_create_form.html"

class IngredientUpdate(UpdateView):
   model = Ingredient
   template_name = "inventory/ingr_update_form.html"
   form_class = IngredientUpdateForm

class IngredientDelete(DeleteView):
   model = Ingredient
   template_name = "inventory/ingr_delete_form.html"
   success_url = "/ingr/"

class RecipeCreate(CreateView):
  model = RecipeRequirement
  form_class = RecipeReqCreateForm
  template_name = "inventory/recipe_create_form.html"

class RecipeUpdate(UpdateView):
   model = RecipeRequirement
   template_name = "inventory/recipe_update_form.html"
   form_class = RecipeReqUpdateForm

class RecipeDelete(DeleteView):
   model = RecipeRequirement
   template_name = "inventory/recipe_delete_form.html"
   success_url = "/recipe/"
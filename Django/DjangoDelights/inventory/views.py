from django.shortcuts import render, redirect
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemCreateForm, MenuItemUpdateForm, IngredientCreateForm, IngredientUpdateForm, RecipeReqCreateForm, RecipeReqUpdateForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def menu(request):
    menu = MenuItem.objects.all()
    context = {"menuitems" : menu }
    return render(request, "inventory/menu.html", context)

def logout_request(request):
  logout(request)
  return redirect("menu")

@login_required
def menutable(request):
    menu = MenuItem.objects.all()
    context = {"menuitems" : menu }
    return render(request, "inventory/menutable.html", context)

@login_required
def ingr(request):
  all_ingredients = Ingredient.objects.all()
  context = {"ingredients" : all_ingredients}
  return render(request, 'inventory/ingr.html', context)

@login_required
def recipe(request):
    recreqs = RecipeRequirement.objects.all()
    context = {"recreq" : recreqs}
    return render(request, "inventory/recipe.html", context)

@login_required
def purchasesuccess(request):
    return render(request, "inventory/purchasesuccess.html")

@login_required
def purchasefailure(request):
    return render(request, "inventory/purchasefailure.html")

class Purch(LoginRequiredMixin, TemplateView):
   template_name = "inventory/purch.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      purch = Purchase.objects.all()
      context["purchases"] = purch
      revenue = 0
      expenses = 0
      for sale in purch:
         revenue += sale.menu_item.menuitemPrice
         requirements = sale.menu_item.reciperequirement_set
         for req in requirements.all():
            expenses += req.quantity*req.ingredient.ingredientPrice
      context["revenue"] = revenue
      context["profit"] = revenue - expenses
      return context

class PurchaseItem(LoginRequiredMixin, TemplateView):
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

class MenuItemCreate(LoginRequiredMixin, CreateView):
  model = MenuItem
  form_class = MenuItemCreateForm
  template_name = "inventory/menuitem_create_form.html"

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
   model = MenuItem
   template_name = "inventory/menuitem_update_form.html"
   form_class = MenuItemUpdateForm

class MenuItemDelete(LoginRequiredMixin, DeleteView):
   model = MenuItem
   template_name = "inventory/menuitem_delete_form.html"
   success_url = "/"

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/ingr_create_form.html"

class IngredientUpdate(LoginRequiredMixin, UpdateView):
   model = Ingredient
   template_name = "inventory/ingr_update_form.html"
   form_class = IngredientUpdateForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
   model = Ingredient
   template_name = "inventory/ingr_delete_form.html"
   success_url = "/ingr/"

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = RecipeRequirement
  form_class = RecipeReqCreateForm
  template_name = "inventory/recipe_create_form.html"

class RecipeUpdate(LoginRequiredMixin, UpdateView):
   model = RecipeRequirement
   template_name = "inventory/recipe_update_form.html"
   form_class = RecipeReqUpdateForm

class RecipeDelete(LoginRequiredMixin, DeleteView):
   model = RecipeRequirement
   template_name = "inventory/recipe_delete_form.html"
   success_url = "/recipe/"
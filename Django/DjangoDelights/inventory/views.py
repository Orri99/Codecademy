from django.shortcuts import render
from .models import Ingredient
from .forms import IngredientCreateForm, IngredientUpdateForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def menu(request):
    return render(request, "inventory/menu.html")

def ingr(request):
  all_ingredients = Ingredient.objects.all()
  context = {"ingredients" : all_ingredients}
  return render(request, 'inventory/ingr.html', context)

def recipe(request):
    return render(request, "inventory/recipe.html")

def purch(request):
    return render(request, "inventory/purch.html")

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
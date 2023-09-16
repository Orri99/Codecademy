from django.db import models
import datetime

# Create your models here.

class MenuItem(models.Model):
    appetizer = "APET"
    maincourse = "MAIN"
    dessert = "DSRT"
    side = "SIDE"
    drink = "DRNK"
    ITEM_CHOICES = [
        (appetizer, "Appetizer"),
        (maincourse, "Main Course"),
        (dessert, "Dessert"),
        (side, "Side"),
        (drink, "Drink"),
    ]

    menuitemName = models.CharField(max_length=50,verbose_name="Menu Item")
    menuitemPrice = models.FloatField(default=20.0, verbose_name="Price")
    menuitemCategory = models.CharField(max_length=4, choices=ITEM_CHOICES,default=drink)

    def purchaseItem(self):
        try:
            Purchase.objects.create(menu_item=self)
            return True
        except:
            return False

    def __str__(self):
        return '{}'.format(self.menuitemName)
    
    def get_absolute_url(self):
        return "/menutable/"

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=50, verbose_name="Ingredient")
    ingredientStock = models.IntegerField(default=0, verbose_name="Amount in stock")
    ingredientUnit = models.CharField(max_length=10, default="?", verbose_name="Unit")
    ingredientPrice = models.FloatField(default=0, verbose_name="Price")
    
    def __str__(self):
        return '{}'.format(self.ingredientName)
    
    def get_absolute_url(self):
        return "/ingr/"
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name="Menu Item", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, verbose_name="Ingredient", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0, verbose_name="Quantity")

    def __str__(self):
        return 'Amount of {} in {}'.format(self.menu_item.menuitemName, self.ingredient.ingredientName)
    
    def get_absolute_url(self):
        return "/recipe/"
    
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name="Menu item", on_delete=models.PROTECT)
    timestamp = models.DateTimeField(verbose_name="Timestamp", null=True, auto_now_add=True)

    def __str__(self):
        return 'Purchase of {}'.format(self.menu_item.menuitemName)
    
    def get_absolute_url(self):
        return "/purch/"
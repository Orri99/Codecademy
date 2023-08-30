from django.db import models

# Create your models here.

class MenuItem(models.Model):
    menuitemName = models.CharField(max_length=50,verbose_name="Menu Item")
    menuitemPrice = models.FloatField(default=20.0, verbose_name="Price")

    def __str__(self):
        return '{}'.format(self.menuitemtName)
    
    def get_absolute_url(self):
        return "/"

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=50, verbose_name="Ingredient")
    ingredientStock = models.IntegerField(default=0, verbose_name="Amount in stock")
    ingredientUnit = models.CharField(max_length=10, default="?", verbose_name="Unit")
    ingredientPrice = models.FloatField(default=0, verbose_name="Price")
    
    def __str__(self):
        return '{}'.format(self.ingredientName)
    
    def get_absolute_url(self):
        return "/ingr/"
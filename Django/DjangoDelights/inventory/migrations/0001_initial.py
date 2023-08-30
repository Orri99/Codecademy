# Generated by Django 4.2 on 2023-08-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientName', models.CharField(max_length=50, verbose_name='Ingredient')),
                ('ingredientPrice', models.FloatField(default=0, verbose_name='Price')),
                ('ingredientStock', models.IntegerField(default=0, verbose_name='Amount in stock')),
            ],
        ),
    ]

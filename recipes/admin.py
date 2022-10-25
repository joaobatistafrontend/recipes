from django.contrib import admin
from .models import Category,Recipe



class CategoryAdm(admin.ModelAdmin):
    ...
    
admin.site.register(Category, CategoryAdm)

@admin.register(Recipe)
class RecipeAdm(admin.ModelAdmin):
    ...


import django_filters 
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)

class RecipeFilter(django_filters.FilterSet):
    """docstring for RecipeFilter."""
    
    class Meta:
        model = Recipe
        fields = {'title': ['exact','contains'],
                'description': ['exact', 'contains'],
                'price': ['exact', 'lt','gt','range'],
                'time_minutes': ['exact', 'lt','gt','range']}

    

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price']
        read_only_fields = ['id']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(_("Product name must be at least 3 characters long."))
        return value
    
    def create(self, validated_data):
        """Create a product."""
        product = Product.objects.create(**validated_data)
        return product
    
class ProductImageSerializer(serializers.ModelSerializer):
    pass
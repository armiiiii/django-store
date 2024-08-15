from rest_framework import serializers

from .models import Product, ProductImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("product", )


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=True)
    
    class Meta:
        model = Product
        fields = "__all__"
        expanded_fields = ["images"]

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ProductSerializer, self).get_field_names(declared_fields, info)
        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

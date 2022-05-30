from urllib import request
from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description',
                  'image_link', 'published', 'category', 'updated')

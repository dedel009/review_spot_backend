from rest_framework import serializers

from category.models import Category


# 상품 시리얼라이저
class CategoryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

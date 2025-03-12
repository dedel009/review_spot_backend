from rest_framework import serializers

from category.serializers import CategoryAllSerializer
from product.models import Product


# 상품 시리얼라이저
class ProductAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# 상품 리스트 응답 시리얼라이저
class ProductListResponseSerializer(serializers.ModelSerializer):

    # 상품 ID
    def get_product_id(self, instance: Product):
        return instance.pk

    # 상품 이미지 경로
    def get_img_path(self, instance: Product):
        return instance.imgPath

    # 상품명
    def get_product_name(self, instance: Product):
        return instance.name

    # 카테고리
    def get_category(self, instance: Product):
        return CategoryAllSerializer(instance=instance.category).data

    # 양주 용량
    def get_capacity(self, instance: Product):
        return instance.product_info.get('capacity', 0)

    # 양주 도수
    def get_alcohol(self, instance: Product):
        return instance.product_info.get('alcohol', 0)

    # 양주 생산지
    def get_area(self, instance: Product):
        return instance.product_info.get('area', '')

    product_id = serializers.SerializerMethodField()
    img_path = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    capacity = serializers.SerializerMethodField()
    alcohol = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'product_id',
            'img_path',
            'product_name',
            'category',
            'capacity',
            'alcohol',
            'area',
        ]


# 상품 상세보기 응답 시리얼라이저
class ProductDetailResponseSerializer(serializers.ModelSerializer):

    def get_product_id(self, instnace: Product):
        return instnace.pk

    def get_img_path(self, instance: Product):
        return instance.imgPath

    def get_product_name(self, instance: Product):
        return instance.name

    def get_category(self, instance: Product):
        return CategoryAllSerializer(instance=instance.category).data

    def get_capacity(self, instance: Product):
        return instance.product_info.get('capacity', 0)

    def get_alcohol(self, instance: Product):
        return instance.product_info.get('alcohol', 0)

    def get_area(self, instance: Product):
        return instance.product_info.get('area', '')

    def get_distillery(self, instance: Product):
        return instance.product_info.get('distillery', '')

    def get_bottler(self, instance: Product):
        return instance.product_info.get('bottler', '')

    def get_bottling_serie(self, instance: Product):
        return instance.product_info.get('bottling_serie', '')

    def get_bottled(self, instance: Product):
        return instance.product_info.get('bottled', '')

    def get_cask_type(self, instance: Product):
        return instance.product_info.get('cask_type', '')

    # 상품 ID
    product_id = serializers.SerializerMethodField()
    # 상품 이미지 경로
    img_path = serializers.SerializerMethodField()
    # 상품 이름
    product_name = serializers.SerializerMethodField()
    # 상품 카테고리
    category = serializers.SerializerMethodField()
    # 용량
    capacity = serializers.SerializerMethodField()
    # 도수
    alcohol = serializers.SerializerMethodField()
    # 생산지
    area = serializers.SerializerMethodField()
    # 증류소
    distillery = serializers.SerializerMethodField()
    # 병입업자
    bottler = serializers.SerializerMethodField()
    # 병입 시리즈
    bottling_serie = serializers.SerializerMethodField()
    # 병입년도
    bottled = serializers.SerializerMethodField()
    # 오크통 유형
    cask_type = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'product_id',
            'img_path',
            'product_name',
            'category',
            'capacity',
            'alcohol',
            'area',
            'distillery',
            'bottler',
            'bottling_serie',
            'bottled',
            'cask_type',
        ]
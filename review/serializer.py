from rest_framework import serializers
from product.serializers import ProductAllSerializer
from review.models import Review


# 리뷰 응답 시리얼라이저
class ReivewListResponseSerializer(serializers.ModelSerializer):

    def get_review_id(self, instance: Review):
        return instance.pk

    # 리뷰 작성자 별명
    # def get_nickname(self, instance: Review):
    #     return instance.nickname

    def get_avg_score(self, instance: Review):
        total_score = 0
        total_score += instance.review_score_info.get('nose_score', 0)
        total_score += instance.review_score_info.get('palate_score', 0)
        total_score += instance.review_score_info.get('finish_score', 0)

        avg_score = total_score / len(instance.review_score_info)
        return avg_score

    def get_nose_score(self, instance: Review):
        return instance.review_score_info.get('nose_score', 0)

    def get_palate_score(self, instance: Review):
        return instance.review_score_info.get('palate_score', 0)

    def get_finish_score(self, instance: Review):
        return instance.review_score_info.get('finish_score', 0)

    def get_product(self, instance: Review):
        return ProductAllSerializer(instance=instance.product).data

    # def get_content(self, instance: Review):
    #     return instance.content

    # def get_aroma_profile(self, instance: Review):
    #     return instance.aroma_profile

    review_id = serializers.SerializerMethodField()
    # nickname = serializers.SerializerMethodField()
    avg_score = serializers.SerializerMethodField()
    nose_score = serializers.SerializerMethodField()
    palate_score = serializers.SerializerMethodField()
    finish_score = serializers.SerializerMethodField()
    # content = serializers.SerializerMethodField()
    # aroma_profile = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'review_id',
            'nickname',
            'avg_score',
            'nose_score',
            'palate_score',
            'finish_score',
            'content',
            'aroma_profile',
            'product',
        ]


# 리뷰 작성 요청 시리얼라이저
class CreateReviewRequestSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField(
        help_text='상품 ID'
    )
    user_id = serializers.CharField(
        help_text='유저 ID'
    )
    nickname = serializers.CharField(
        help_text='리뷰 작성자 닉네임'
    )
    nose_score = serializers.IntegerField(
        help_text='향 점수'
    )
    palate_score = serializers.IntegerField(
        help_text='맛 점수'
    )
    finish_score = serializers.IntegerField(
        help_text='피니쉬 점수'
    )
    content = serializers.CharField(
        help_text='리뷰 내용'
    )
    aroma_profile = serializers.JSONField(
        help_text='방사형 차트에 쓰이는 데이터'
    )

    class Meta:
        model = Review
        fields = [
            'product_id',
            'user_id',
            'nickname',
            'nose_score',
            'palate_score',
            'finish_score',
            'content',
            'aroma_profile'
        ]

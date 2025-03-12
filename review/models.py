from django.db import models


# 리뷰 모델
class Review(models.Model):

    nickname = models.CharField(
        verbose_name='리뷰 작성자 닉네임',
        null=False,
        blank=False,
    )

    content = models.TextField(
        verbose_name='리뷰 내용',
        null=False,
        blank=False,
    )

    review_score_info = models.JSONField(
        verbose_name='리뷰 점수 정보',
        default=dict,
        blank=True,
        null=True,
    )

    aroma_profile = models.JSONField(
        verbose_name='방사형 차트에 쓰이는 데이터'
    )

    created = models.DateTimeField(
        verbose_name='생성일시',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name='수정일시',
        auto_now=True,
    )

    product = models.ForeignKey(
        'product.Product',
        on_delete=models.PROTECT,
    )

    user = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.PROTECT,
    )

    is_active = models.BooleanField(
        verbose_name='사용 유무',
        default=True,
    )

from django.db import models

# Create your models here.


# 양주, 술안주 등 리뷰 대상 제품 모델
class Product(models.Model):
    name = models.CharField(
        verbose_name='제품명',
    )

    imgPath = models.CharField(
        verbose_name='제품 이미지 경로',
        blank=True,
        null=True,
    )

    # 양주는 도수, 용량, 생산지가 들어감
    product_info = models.JSONField(
        verbose_name='제품 정보 관련 데이터',
        default=dict,
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name='생성일시',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name='수정일시',
        auto_now=True,
    )

    category = models.ForeignKey(
        'category.Category',
        on_delete=models.SET_NULL,
        null=True,
    )

    is_active = models.BooleanField(
        verbose_name='사용 유무',
        default=True,
    )

    # alcohol = models.IntegerField(
    #     verbose_name='도수'
    # )
    #
    # capacity = models.IntegerField(
    #     verbose_name='양주 용량'
    # )
    #
    # area = models.CharField(
    #     verbose_name='양주 생산지'
    # )

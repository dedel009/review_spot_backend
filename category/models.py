from django.db import models


# 제품의 카테고리 모델
class Category(models.Model):
    name = models.CharField(
        verbose_name='카테고리명'
    )

    created = models.DateTimeField(
        verbose_name='생성일시',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name='수정일시',
        auto_now=True,
    )

    is_active = models.BooleanField(
        verbose_name='사용 유무',
        default=True,
    )

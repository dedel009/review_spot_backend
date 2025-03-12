from rest_framework import serializers


# 공통 요청 시리얼라이저
class CommonListRequestSerializer(serializers.Serializer):
    query = serializers.CharField(
        help_text='검색어',
        default="",
        required=False,
    )
    # display = serializers.IntegerField(
    #     help_text='한번에 표시할 검색 결과 개수',
    #     default=20
    # )
    category_id = serializers.IntegerField(
        help_text='카테고리 ID',
        default=0,
        required=False,
    )
    sort = serializers.CharField(
        help_text='검색 결과 정렬 방법',
        default='created',
        required=False,
    )
    # pageNum = serializers.IntegerField(
    #     help_text='페이지 번호',
    #     default=0
    # )


class CommonDetailRequestSerializer(serializers.Serializer):

    product_id = serializers.IntegerField(
        help_text='상품 ID',
        required=False,
    )

    # 예시
    category_id = serializers.IntegerField(
        help_text='카테고리 ID',
        required=False,
    )



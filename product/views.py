from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from common.serializer import CommonListRequestSerializer, CommonDetailRequestSerializer
from common.utils import CustomResponse
from product.serializers import ProductListResponseSerializer, ProductDetailResponseSerializer


class ProductListApiView(APIView):

    @swagger_auto_schema(
        query_serializer=CommonListRequestSerializer,
        responses={200: ProductListResponseSerializer(many=True)},
        operation_description="상품 리스트 조회 API",
    )
    # 상품 리스트 조회 API
    def get(self, reqeust: Request, *args, **kwargs):

        # 요청 시리얼라이저로 쿼리 파라미터를 검증
        request_serializer = CommonListRequestSerializer(data=reqeust.query_params)
        request_serializer.is_valid(raise_exception=True)
        print("request_serializer :::", request_serializer.data)

        # 검증된 데이터로 쿼리셋 필터링
        # 검색어
        query_params = request_serializer.validated_data.get('query', '')
        # 카테고리
        category_id = request_serializer.validated_data.get('category_id', 0)
        # 정렬 방법
        sort = request_serializer.validated_data.get('sort', 'created')

        from product.models import Product
        product_qs = Product.objects.filter(
            is_active=True,
        ).select_related(
            'category'
        )

        # 검색어로 상품명 필터링
        if query_params:
            product_qs = product_qs.filter(
                Q(name__icontains=query_params)
            )

        if category_id:
            product_qs = product_qs.filter(
                Q(category_id=category_id)
            )

        if sort == 'created':
            product_qs = product_qs.order_by('-created')
        elif sort == 'id':
            product_qs = product_qs.order_by('-id')

        # 페이지네이션 처리
        from common.utils import CustomPagination
        paginator = CustomPagination()
        paginated_product_list = paginator.paginate_queryset(product_qs, reqeust)

        print("paginated_product_list :::", paginated_product_list)

        if len(paginated_product_list) == 0:
            error_message = '조회된 상품 목록이 없습니다.'
            return paginator.get_paginated_response(status=status.HTTP_400_BAD_REQUEST, data=error_message)

        # 응답 시리얼라이저로 데이터 직렬화
        response_product_list_serializer = ProductListResponseSerializer(paginated_product_list, many=True)

        return paginator.get_paginated_response(status=status.HTTP_200_OK, data=response_product_list_serializer.data)


# 상품 상세 정보 조회 API
class ProductDetailApiView(APIView):

    @swagger_auto_schema(
        query_serializer=CommonDetailRequestSerializer,
        responses={status.HTTP_200_OK: '성공'},
        operation_description="상품 상세보기 조회 API",
    )
    def get(self, reqeust: Request, *args, **kwargs):

        # 요청 시리얼라이저로 쿼리 파라미터를 검증
        request_serializer = CommonDetailRequestSerializer(data=reqeust.query_params)
        request_serializer.is_valid(raise_exception=True)
        print("request_serializer :::", request_serializer.data)

        product_id = request_serializer.validated_data.get('product_id')

        # 해당하는 상품 쿼리셋
        from product.models import Product
        product_qs = Product.objects.filter(
            id=product_id,
            is_active=True,
        )

        # 상품 상세보기 데이터가 없을 경우 에러 반환
        if not product_qs.exists():
            return CustomResponse(code="CODE_0001")

        return CustomResponse(data=ProductDetailResponseSerializer(instance=product_qs.first(), many=False).data)





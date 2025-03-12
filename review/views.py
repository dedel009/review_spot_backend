from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from common.serializer import CommonListRequestSerializer
from product.models import Product
from review.serializer import ReivewListResponseSerializer, CreateReviewRequestSerializer
from user.models import CustomUser


# 리뷰 작성 및 리스트 조회 API
class ReviewAPIView(APIView):

    # HTTP 요청이 들어올 때 호출되는 메서드
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            # POST 요청에 대해서만 JWT 인증과 권한 검사 적용
            from common.authentication import CustomJWTAuthentication
            self.authentication_classes = [CustomJWTAuthentication]
            self.permission_classes = [IsAuthenticated]

        # 부모 클래스의 dispatch 메서드를 호출하여 적절한 핸들러로 요청을 전달
        return super().dispatch(request, *args, **kwargs)

    @swagger_auto_schema(
        query_serializer=CommonListRequestSerializer(),
        responses={200: ReivewListResponseSerializer(many=True)},
        operation_description="리뷰 리스트 조회 API",
    )
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

        from review.models import Review
        review_queryset = Review.objects.filter(
            is_active=True,
        )

        # 리뷰 내용 필터
        if query_params:
            review_queryset = review_queryset.filter(
                Q(content__contains=query_params)
            )

        # 카테고리 필터
        if category_id:
            review_queryset = review_queryset.filter(
                Q(product__category_id=category_id)
            )

        # 정렬 처리
        if sort == 'created':
            review_queryset = review_queryset.order_by('-created')
        elif sort == 'id':
            review_queryset = review_queryset.order_by('-id')

        # 페이지네이션 처리
        from common.utils import CustomPagination
        paginator = CustomPagination()
        paginated_review_list = paginator.paginate_queryset(review_queryset, reqeust)

        print("paginated_review_list :::", paginated_review_list)

        if len(paginated_review_list) == 0:
            error_message = '조회된 리뷰 목록이 없습니다.'
            return paginator.get_paginated_response(status=status.HTTP_400_BAD_REQUEST, data=error_message)

        # 응답 시리얼라이저로 데이터 직렬화
        response_review_list_serializer = ReivewListResponseSerializer(paginated_review_list, many=True)

        return paginator.get_paginated_response(status=status.HTTP_200_OK, data=response_review_list_serializer.data)

    @swagger_auto_schema(
        request_body=CreateReviewRequestSerializer,
        responses={200: '성공'},
        operation_description="리뷰 작성 API",
    )
    def post(self, reqeust: Request, *args, **kwargs):

        request_serializer = CreateReviewRequestSerializer(data=reqeust.data)
        request_serializer.is_valid(raise_exception=True)
        print("request_serializer :::", request_serializer.data)

        product_id = request_serializer.validated_data.get('product_id', 0)
        user_id = request_serializer.validated_data.get('user_id')

        # 생성 파라미터
        create_params = {
            'nickname': request_serializer.validated_data.get('nickname', ''),
            'content': request_serializer.validated_data.get('content', ''),
            'review_score_info': {
                'nose_score': request_serializer.validated_data.get('nose_score', 0),
                'palate_score': request_serializer.validated_data.get('palate_score', 0),
                'finish_score': request_serializer.validated_data.get('finish_score', 0),
            },
            'aroma_profile': request_serializer.validated_data.get('aroma_profile', dict),
        }

        # 상품 데이터 유효성 검증
        from common.utils import CustomResponse
        try:
            product_qs = Product.objects.filter(
                id=product_id,
                is_active=True,
            )

            user_qs = CustomUser.objects.filter(
                is_active=True,
                username=user_id,
            )

            if all([product_qs.exists(), user_qs.exists()]):
                create_params['product'] = product_qs.first()
                create_params['user'] = user_qs.first()
                # 리뷰 데이터 생성
                from review.models import Review
                Review.objects.create(**create_params)
                return CustomResponse(code='CODE_0000')
            else:
                return CustomResponse(code='CODE_0001')
        except Exception as e:
            print(f'예기치 못한 에러명 : {e}')
            return CustomResponse(code='CODE_0002')

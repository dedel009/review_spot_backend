from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from common.utils import CustomResponse
from user.serializers import LoginRequestSerializer, TokenRefreshRequestSerializer, LoginResponseSerializer, \
    TokenRefreshResponseSerializer, DuplicationUserIdRequestSerializer, DuplicationUserIdResponseSerializer, \
    UserSignUpAPIRequestSerializer


class CustomLoginAPIView(APIView):
    """
    사용자 계정만 사용하는 API(추후 관리자 계정 로그인 API 개발 예정)
    """

    @swagger_auto_schema(
        request_body=LoginRequestSerializer,
        responses={
            200: openapi.Response('로그인 성공', LoginResponseSerializer),
        },
        operation_description="로그인 API",
    )
    def post(self, request: Request):
        # 요청 시리얼라이저로 쿼리 파라미터를 검증
        request_serializer = LoginRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        # 유저 아이디
        username = request_serializer.validated_data.get('username')
        # 유저 패스워드
        password = request_serializer.validated_data.get('password')

        # 해당 유저가 있는지 없는지 검증
        from .models import CustomUser
        user_qs = CustomUser.objects.filter(
            username=username,
            is_active=True,
            is_staff=False,  # 일반 사용자만 조회
        )

        # 유저가 없을 경우
        if not user_qs.exists():
            return CustomResponse(code='CODE_0001', status_code=status.HTTP_401_UNAUTHORIZED)

        user_instance: CustomUser = user_qs.first()

        # 비밀번호 검증
        if not user_instance.check_password(password):
            return CustomResponse(code='CODE_0003', status_code=status.HTTP_401_UNAUTHORIZED)

        # jwt 토큰 발급
        refresh_token = RefreshToken.for_user(user_instance)
        refresh_token['username'] = user_instance.username
        token_params = {
            'refresh_token': str(refresh_token),
            'access_token': str(refresh_token.access_token)
        }
        return CustomResponse(code='CODE_0000', data=LoginResponseSerializer(instance=token_params, many=False).data)


class TokenRefreshAPIView(APIView):
    """
    리프래쉬 토큰을 통해 액세스 토큰을 재발급하는 API
    """

    @swagger_auto_schema(
        request_body=TokenRefreshRequestSerializer,
        responses={
            200: openapi.Response('토큰 재발급 성공', TokenRefreshResponseSerializer),
        },
        operation_description="토큰 재발급 API",
    )
    def post(self, request, *args, **kwargs):
        # 클라이언트에서 리프레시 토큰 가져오기
        refresh_token = request.data.get('refresh_token', '')

        print("refresh_token :::", refresh_token)
        if not refresh_token:
            return CustomResponse(code='CODE_0005', status_code=status.HTTP_400_BAD_REQUEST)

        try:
            # RefreshToken 클래스 사용해 토큰 검증 및 새 액세스 토큰 생성
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token

            return CustomResponse(data=TokenRefreshResponseSerializer(instance={'access_token': str(access_token)}, many=False).data)

        except TokenError as e:
            # 토큰이 유효하지 않거나 만료된 경우 예외 처리
            return CustomResponse(code='CODE_0006', status_code=status.HTTP_401_UNAUTHORIZED)


class UserSignUpAPIView(APIView):
    """
    유저 회원가입 API
    """
    @swagger_auto_schema(
        request_body=UserSignUpAPIRequestSerializer,
        responses={
            200: openapi.Response('유저 회원 가입 성공'),
        },
        operation_description="회원 가입 API",
    )
    def post(self, request):
        # 요청 시리얼라이저로 쿼리 파라미터를 검증
        request_serializer = UserSignUpAPIRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        user_id = request_serializer.validated_data.get('user_id')
        password = request_serializer.validated_data.get('password')
        name = request_serializer.validated_data.get('name')
        email = request_serializer.validated_data.get('email')
        nickname = request_serializer.validated_data.get('nickname')

        from user.models import CustomUser
        try:
            CustomUser.objects.create_user(
                username=user_id,
                password=password,
                name=name,
                email=email if email else None,
                nickname=nickname if nickname else None,
            )
        except IntegrityError as e:
            # 예: 사용자 이름이 중복될 때 발생
            # 예외 처리 로직 추가
            print(f"데이터베이스 에러: {e}")
        except ValidationError as e:
            # 예: 입력값 유효성 검사 실패 시 발생
            print(f"유효성 검사 에러: {e}")
        except Exception as e:
            # 그 외의 예상치 못한 예외 처리
            print(f"예상치 못한 에러: {e}")

        return CustomResponse(code="CODE_0009")


class DuplicationUserIdView(APIView):
    """
    아이디 중복 체크 API
    """
    @swagger_auto_schema(
        request_body=DuplicationUserIdRequestSerializer,
        responses={
            200: openapi.Response('유저 ID 중복 체크 성공', DuplicationUserIdResponseSerializer),
        },
        operation_description="유저 ID 중복 체크 API",
    )
    def post(self, request):
        # 요청 시리얼라이저로 쿼리 파라미터를 검증
        request_serializer = DuplicationUserIdRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        # 유저 ID
        user_id = request_serializer.validated_data.get('user_id')

        from user.models import CustomUser
        user_qs = CustomUser.objects.filter(
            username=user_id,
            is_active=True,
        )

        # 해당하는 유저가 없을 경우
        if not user_qs.exists():
            return CustomResponse(
                data=DuplicationUserIdResponseSerializer(
                    instance={
                        'duplication_check_flag':False
                    }
                ).data,
                code="CODE_0007"
            )
        else:
            return CustomResponse(
                data=DuplicationUserIdResponseSerializer(
                    instance={
                        'duplication_check_flag':True
                    }
                ).data,
                code="CODE_0008"
            )
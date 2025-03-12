from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication, AuthUser
from rest_framework_simplejwt.tokens import Token


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token: Token) -> AuthUser:
        """
        JWT 토큰에서 유저 ID를 추출하고, customuser 모델을 참조하여 유저를 반환.
        """
        try:
            # 기본적으로 id는 토큰의 user_id 필드에 저장
            user_id = validated_token.get('user_id')

            # CustomUser 모델에서 사용자 검색
            from user.models import CustomUser
            user = CustomUser.objects.get(pk=user_id)

            print("user_instance :::", user)

        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('해당 사용자가 존재하지 않습니다.')

        if not user.is_active:
            raise AuthenticationFailed('해당 사용자는 비활성화 상태입니다.')

        return user


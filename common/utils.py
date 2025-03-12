import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import BasePermission


# 커스텀 페이지 네이션 클래스
class CustomPagination(PageNumberPagination):
    # 페이지 번호
    page_query_param = 'page_num'
    # 페이지 크기
    page_size_query_param = 'display'
    # 기본 페이지 크기
    page_size = 20
    # 최대 페이지 크기
    # max_page_size = 100

    def get_paginated_response(self, data, **kwargs):
        return_status = kwargs.get('status', status.HTTP_200_OK)
        return Response({
            'success': True,
            'message': '성공' if return_status == status.HTTP_200_OK else data,
            'total_item': self.page.paginator.count if return_status == status.HTTP_200_OK else None,
            'data': data if return_status == status.HTTP_200_OK else None,
        })


# 응답 반환 메소드
def CustomResponse(code='CODE_0000', data=None, status_code=status.HTTP_200_OK):

    return_message = GetCustomCode(code)

    return Response({
        'success': True,
        'message': return_message,
        'data': data,
    }, status=status_code)


# 메세지 반환 메소드
def GetCustomCode(code):
    if code == 'CODE_0000':
        return "성공"
    elif code == 'CODE_0001':
        return "존재하지 않는 대상입니다."
    elif code == 'CODE_0002':
        return "예기치 못한 에러입니다. 다시 시도해주세요."
    elif code == 'CODE_0003':
        return "비밀번호가 일치하지 않습니다."
    elif code == 'CODE_0004':
        return "인증되지 않은 요청입니다."
    elif code == 'CODE_0005':
        return "리프레시 토큰이 제공되지 않았습니다."
    elif code == 'CODE_0006':
        return "유효하지 않은 리프레시 토큰입니다."
    elif code == 'CODE_0007':
        return "중복된 아이디가 없습니다."
    elif code == 'CODE_0008':
        return "중복된 아이디입니다."
    elif code == 'CODE_0009':
        return "정상적으로 회원가입이 완료되었습니다."




"""
URL configuration for review_spot_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import mimetypes
import os

from django.contrib import admin
from django.urls import path, include
# swagger 설정
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

# swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        # API 제목
        title='Review Spot Backend API',
        # API 기본 버전
        default_version='v1',
        # API에 대한 상세 설명
        description='리뷰스팟 백엔드 관련 API 문서',
        # API 사용에 대한 서비스 약관 URL
        terms_of_service='https://www.google.com/policies/terms/',
        # API 제공자와 연락할 수 있는 정보
        contact=openapi.Contact(email="dedel009@ronfic.com"),
        # API 라이선스 정보 제공
        license=openapi.License(name="Review Spot License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),    # 관리자 페이지 URL

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Django REST Framework의 기본 API 뷰를 설정
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('silk/', include('silk.urls', namespace='silk')),

    # 사용자가 추가한 앱 url
    # 제품 url
    path('api/products/', include('product.urls')),
    # 리뷰 url
    path('api/reviews', include('review.urls')),
    # 인증 url
    path('api/', include('user.urls')),

]

env = os.environ.get('DJANGO_ENV', 'development')
print("env :::", env)
if env == 'development':
    mimetypes.add_type('application/javascript', '.js', True)
    if settings.DEBUG:
        print("debug mode is on. Debug Toolbar is included.")
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls))
        ]


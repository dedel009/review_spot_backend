from django.urls import path, include

from review import views

urlpatterns = [
    # 리뷰 작성 API
    path('', views.ReviewAPIView.as_view(), name='review-list')
]

from django.urls import path

from product import views

urlpatterns = [
    # 상품 리스트 조회
    path('', views.ProductListApiView.as_view(), name='product-list'),
    # 상품 상세정보 조회
    path('detail', views.ProductDetailApiView.as_view(), name='product-detail'),

]

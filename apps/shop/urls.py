from django.urls import path

from .views import ShopListCreateAPIView, ShopDetailAPIView


urlpatterns = [
    path('', ShopListCreateAPIView.as_view(), name='shop-list'),
    path('<int:pk>/', ShopDetailAPIView.as_view(), name='shop-detail'),
]
from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, CategoryProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'categories/(?P<id>[0-9]+)/products/', CategoryProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

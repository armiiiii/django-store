from django.contrib import admin
from django.urls import path

from rest_framework.routers import SimpleRouter

from goods.views import ProductViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

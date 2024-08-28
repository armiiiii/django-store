from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from goods.views import ProductViewSet
from users.views import UserViewset, retrieve_feedbacks


router = SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('feedbacks/<int:prod_id>/', retrieve_feedbacks, name="feedbacks")]

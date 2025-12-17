from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import VehicleViewSet, EmployeeViewSet, ExpenseViewSet, LocationPointViewSet

router = routers.DefaultRouter()
router.register(r"vehicles", VehicleViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"expenses", ExpenseViewSet)
router.register(r"locations", LocationPointViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import BlockedCallViewSet, CustomAuthToken, RegisterView, ChatView, AdminStatsView

router = DefaultRouter()
router.register(r'blocked-calls', BlockedCallViewSet, basename='blocked-calls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', CustomAuthToken.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/chat/', ChatView.as_view()),
    path('api/admin/stats/', AdminStatsView.as_view()),
    path('api/', include(router.urls)),
]

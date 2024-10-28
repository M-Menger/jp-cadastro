from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewsets,views
from django.conf import settings
from django.conf.urls.static import static

route = routers.DefaultRouter()

route.register(r'membros', viewsets.MembroViewSet, basename='Membro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('membros/', views.MembroAPIView.as_view(), name='membros-list-create'),
    path('membro/<int:pk>', views.MembroAPIView.as_view(), name='membros-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API Router
router = DefaultRouter()
router.register(r'ipo', views.IPOViewSet)

# Web URLs
urlpatterns = [
    # Web routes
    path('', views.home, name='home'),
    path('list/', views.ipo_list, name='ipo_list'),
    path('detail/<int:ipo_id>/', views.ipo_detail, name='ipo_detail'),
    path('api-docs/', views.api_docs, name='api_docs'),
    
    # API routes
    path('api/', include(router.urls)),
] 
from django.urls import path, include
from django.contrib.auth.models import User

from . import views

from rest_framework import routers, serializers, viewsets


# router = routers.DefaultRouter()
# router.register('awards/', views.api_view, name='/')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('awards/<int:pk>/', views.AwardVew.as_view()),
    path('awards/search/', views.search, name='search'),
    path('api/awards/', views.api_awards),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

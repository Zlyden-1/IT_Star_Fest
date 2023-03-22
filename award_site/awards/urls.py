from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('awards/<int:pk>/', views.AwardVew.as_view()),
    path('awards/search/', views.search, name='search'),
]

from django.urls import path, include
from . import views, filters
from knox import views as knox_views


urlpatterns = [
    path('', views.api_root),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/employees/', views.WorkerList.as_view(), name='employees'),

    ]
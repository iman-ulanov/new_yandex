"""yandex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from accounts import views as acc_views

# acc_router = DefaultRouter()
# acc_router.register('register', acc_views.AuthorRegisterAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/accounts/token/', obtain_auth_token),

    path('api/accounts/', acc_views.AuthorRegisterAPIView.as_view()),
    path('api/accounts/<int:pk>/', acc_views.AuthorRegisterRetrieveUpdateDestroyAPIView.as_view())


]

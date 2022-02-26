"""price_comparison URL Configuration

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
from price_app.views import IndexView,RegistrationView,Login
from django.conf.urls.static import static
from price_comparison import settings
from price_app import user_urls

urlpatterns = [
    path('admin/',include('price_app.admin_urls') ),
    path('user/',include('price_app.user_urls')),
    path('', IndexView.as_view()),
    path('registration',RegistrationView.as_view()),
    path('login',Login.as_view())
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

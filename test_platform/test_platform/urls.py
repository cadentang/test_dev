"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from user_app import views
from user_app.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    #path('login_action/', views.login_action),
    path('login_action/', LoginView.as_view(), name="login"),
    #path('project_manage/', views.project_manage),
	path('logout_view/', views.logout_view),
	path('manage/', include('project_app.urls')),


]

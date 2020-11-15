"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

import app1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.views.home, name='home'),
    path('main/', app1.views.main, name='main'),
    path('main/left', app1.views.left, name='left'),
    path('main/right', app1.views.right, name='right'),
	path('main2/', app1.views.main2, name='main2'),
	path('stream/', app1.views.stream, name='stream'),
]



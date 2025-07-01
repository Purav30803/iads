"""
URL configuration for mysiteS25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

from myapp.views import home_view
from myapp import views
from myapp import view1
urlpatterns = [
    # path('myapp/',include('myapp.urls1')),
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('home/',views.home_view),
    path('',view1.index),
    path('about/',views.about_view),
]

"""
URL configuration for config configject.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoconfigject.com/en/4.2/topics/http/urls/
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
from .settings import base
# from user.views import UserListCreate, UserDetail


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('product.urls')),
    path('api/v1/', include('user.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
#
# if base.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include(debug_toolbar.urls))

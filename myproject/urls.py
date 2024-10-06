"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index',views.index),
    path('',views.first),
    path('userreg',views.userreg),
    path('viewuser',views.viewuser),
    path('usercontact',views.usercontact),
    path('viewcontact',views.viewcontact),
    path('userlogin',views.userlogin),
    path('logout',views.logout),
    path('viewprofile',views.viewprofile),
    path('adminprofile',views.adminprofile),
    path('delete/<int:id>',views.delete, name='delete'),
    path('dele/<int:id>',views.dele, name='dele'),
    path('update/<int:id>',views.update, name='update'),
    path('update/upt/<int:id>',views.upt, name='upt'),
    path('change/<int:id>',views.change, name='change'),
    path('change/ch/<int:id>',views.ch, name='ch'),
   
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                                                                                                                 
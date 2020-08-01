"""JobsPortal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from testapp import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path("Hyd_Jobs.html",views.hyd_Jobs),
    path("Banglore_Jobs.html",views.banglore_Jobs),
    path("Pune_Jobs.html",views.pune_Jobs),
    path("Chennai_Jobs.html",views.chennai_Jobs),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout',views.logout_view),
    path("signup",views.signup_view),
    path('postjob',views.postjob_view),
    path('posthydjob',views.Posthydjobs_view),
    path('postchennaijob',views.PostChennaijobs_view),
    path('postbanglorejob',views.PostBanglorejobs_view),
    path('postpunejob',views.PostPunejobs_view),
    path('thanku', views.thanku_view),
    path('about', views.about_view),
]

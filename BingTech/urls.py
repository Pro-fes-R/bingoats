"""
URL configuration for BingTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bingApp import views



admin.site.site_header = "Bing Technologies LLC Admin"
admin.site.site_title = "Bing Technologies Admin Portal"
admin.site.index_title = "Welcome to Bing Technologies Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.getEmployees, name='list'),
    path('create/', views.createEmployee),
    path('delete/<int:id>', views.DeleteEmployee),
    path('update/<int:id>', views.updateEmployee),
    path('accounts/', include('django.contrib.auth.urls')),
]

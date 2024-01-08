"""
URL configuration for digesto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from appDigesto import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name= 'home'),
    path('signup/', views.signup , name= 'signup'),
    path('logout/',views.out , name='out'),
    path('signin/',views.signin , name='signin'),
    path('createDigesto/',views.createDigesto , name='createDigesto'),
     path('digestos/',views.digestos , name='digestos'),
     path('digesto/<int:id>',views.digesto_detalle , name='digesto_detalle'),
     path('digesto/<int:id>/delete',views.delete_digesto , name='delete_digesto')

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""config URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static 
from django.conf import settings
from home import views
from user import views as UserView


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('login/', UserView.login_form, name='login_form'),
    path('logout/', UserView.logout_form, name='logout_form'),
    path('signup/', UserView.signup_form, name='signup_form'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

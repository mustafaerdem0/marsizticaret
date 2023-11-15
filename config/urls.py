"""
URL configuration for config project.

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
from django.conf import settings


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main_app.views import *
from blog_app.views import *
from contact_app.views import *
from user_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index,name="index"),
    path('product', product,name="product"),
    path('card', card,name="card"),
    path('about', about,name="about"),
    #index end

    #blog app
    path('blog', blog,name="blog"),
    path('blog-detail', blog_detail,name="blog_detail"),
    #blog end


    #contact
    path('contact',contact,name="contact"),
    #contact end



    #user 
    path('login-register',login_register,name='login-register'),
    path('register',user_register,name='user_register'),
    path('login',user_login,name='user_login'),
    #user end


    # filter
    path('product/<category>',productfilter,name='product-filter')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

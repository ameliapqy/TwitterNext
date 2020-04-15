"""twitterNext URL Configuration

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
from core.views import home, delete, deletep, hashtag, hashtagAll, like
from core.views import login_view, signup_view, logout_view, about, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('signout/', logout_view, name='login'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('delete/', delete, name='home'),
    path('deletep/', deletep, name='home'),
    path('hashtag/', hashtag, name='hashtag'),
    path('hashtagAll/', hashtagAll, name='hashtag'),
    path('like/', like, name='home')
]

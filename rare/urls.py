"""
URL configuration for rare project.

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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import register_user, check_user
from rareapi.views import CommentView, TagView, PostTagView, PostView, SubscriptionView, UserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'comments', CommentView, 'comment')
router.register(r'tags', TagView, 'tag')
router.register(r'posttags', PostTagView, 'post_tag')
router.register(r'posts', PostView, 'posts')
router.register(r'subscriptions', SubscriptionView, 'subscription')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),

]

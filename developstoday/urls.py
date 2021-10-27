"""developstoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from news.api import (
    NewsListCreate,
    NewsUpdateDelete,
    NewsUpVote,
    CommentListCreate,
    CommentUpdateDelete,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/news/", NewsListCreate.as_view()),
    path("api/news/<int:pk>/", NewsUpdateDelete.as_view()),
    path("api/news/<int:pk>/upvote/", NewsUpVote.as_view()),
    path("api/news/<int:pk>/comments/", CommentListCreate.as_view()),
    path("api/news/<int:news_pk>/comments/<int:pk>/", CommentUpdateDelete.as_view()),
]

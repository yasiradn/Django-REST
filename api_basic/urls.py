from django.contrib import admin
from django.urls import path
from .views import ArticleAPIView, ArticleAPIDetails, ARGenericAPIView
urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('generic/article/<int:id>', ARGenericAPIView.as_view()),
    #path('article/<int:pk>', article_detail)
    path('article/<int:id>', ArticleAPIDetails.as_view())
]

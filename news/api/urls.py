from django.urls import path
from news.api.views import article_list_create_api_view, article_detail_api_view, ArticleListCreateAPIView, \
    ArticleDetailAPIView, JournalistListCreateAPIView

urlpatterns = [
    path("articles/", article_list_create_api_view, name="article-list"),
    path("articles/<int:pk>", article_detail_api_view, name="article-detail"),
    path("apiview/articles/", ArticleListCreateAPIView.as_view(), name="article-list-APIView"),
    path("apiview/articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article-detail-APIView"),
    path("apiview/journalist/", JournalistListCreateAPIView.as_view(), name="journalist-list-APIView"),
]

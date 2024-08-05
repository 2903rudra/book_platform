from django.urls import path
from .views import BookSearchView, BookListView, RecommendationListView, LikeListView

urlpatterns = [
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('recommendations/', RecommendationListView.as_view(), name='recommendation-list'),
    path('likes/', LikeListView.as_view(), name='like-list'),
]
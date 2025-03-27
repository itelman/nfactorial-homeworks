from django.urls import path

from .views import NewsCreateView, NewsDetailView, NewsDeleteView, NewsListView

urlpatterns = [
    path('api/news/', NewsCreateView.as_view(), name='news-create'),
    path('api/news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('api/news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),
    path('api/news/', NewsListView.as_view(), name='news-list'),
]

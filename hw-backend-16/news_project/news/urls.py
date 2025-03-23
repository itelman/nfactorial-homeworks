from django.urls import path,include

from .views import NewsUpdateView
from .views import news_list, news_detail, add_news
from .views import SignUpView

urlpatterns = [
    path('', news_list, name='news_list'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('add/', add_news, name='add_news'),
    path('104/edit/', NewsUpdateView.as_view(), name='news-edit'),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("accounts/", include("django.contrib.auth.urls")),
path("news/<int:pk>/delete/", NewsDeleteView.as_view(), name="delete-news"),
]

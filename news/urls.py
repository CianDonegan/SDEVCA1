from django.urls import path
from .views import (
    NewsListView,
    NewsUpdateView,
    NewsDetailView,
    NewsDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/',
        NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/delete/',
        NewsDeleteView.as_view(), name='news_delete'),
    path('', NewsListView.as_view(), name='news_list'),
]
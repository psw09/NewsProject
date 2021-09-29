from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('newsDetail', views.newsDetail),
    path('newsInsert', views.newsInsert),
    path('newsInsertVal', views.newsInsertVal),
    path('goodCnt', views.goodCnt),
    path('notGoodCnt', views.notGoodCnt),
    path('newsDelete', views.newsDelete),
]
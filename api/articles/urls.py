from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('article-list/', views.articleList, name='article-list'),
    path('article-detail/<int:pk>/', views.articleDetail, name='article-detail'),
    path('article-create', views.articleCreate, name='article-create'),
    path('article-update/<int:pk>/', views.articleUpdate, name='article-update'),
    path('article-delete/<int:pk>/', views.articleDelete, name='article-delete'),
    path('article-validate/<int:pk>/', views.articleValidate, name='article-validate'),
    path('article-invalidate/<int:pk>/', views.articleInvalidate, name='article-invalidate'),
]
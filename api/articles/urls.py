from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articlesOverview, name='articles-overview'),
    path('all-article-list/', views.allArticleList, name='all-article-list'),
    path('all-article-detail/<int:pk>/', views.allArticleDetail, name='all-article-detail'),
    path('validated-article-list/', views.validatedArticleList, name='validated-article-list'),
    path('validated-article-detail/<int:pk>/', views.validatedArticleDetail, name='validated-article-detail'),
    path('article-create', views.articleCreate, name='article-create'),
    path('article-update/<int:pk>/', views.articleUpdate, name='article-update'),
    path('article-delete/<int:pk>/', views.articleDelete, name='article-delete'),
    path('article-validate/<int:pk>/', views.articleValidate, name='article-validate'),
    path('article-invalidate/<int:pk>/', views.articleInvalidate, name='article-invalidate'),
    path('editions-list/', views.editionsList, name='editions-list'),
]
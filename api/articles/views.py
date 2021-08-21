from .serializers import ArticleSerializer, EditionSerializer
from .models import Article, Edition
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import wget
import os
# Create your views here.

@api_view(['GET'])
def articlesOverview(request):
    articles_urls = {
        'Articles': {
            'Create': '/articles/article-create/ [AUTHENTICATION REQUIRED]',
            'List': '/articles/all-article-list/',
            'Detail': '/articles/all-article-detail/<int:pk>/',
            'List (validated)': '/articles/validated-article-list/',
            'Detail (validated)': '/articles/validated-article-detail/<int:pk>/',
            'Update': '/articles/article-update/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Delete': '/articles/article-delete/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Validate': '/articles/article-validate/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Invalidate': '/articles/article-invalidate/<int:pk>/ [AUTHENTICATION REQUIRED]',
            'Editions List': '/articles/editions-list'
        }
    }

    return Response(articles_urls)


@api_view(['GET'])
def allArticleList(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def validatedArticleList(request):
    articles = Article.objects.filter(validated=True)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allArticleDetail(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def validatedArticleDetail(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)
    if serializer.data['validated'] == True:
        return Response(serializer.data)
    else:
        return Response("Article not validated")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Not registered")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articleUpdate(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=articles, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Not registered")


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def articleDelete(request, pk):
    articles = Article.objects.get(id=pk)
    articles.delete()
    return Response('Successfully deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articleValidate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    serializer2 = ArticleSerializer(instance=article, data=serializer.data)
    if serializer2.is_valid():
        serializer2.validated_data['validated'] = True
        serializer2.save()
    return Response(serializer2.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articleInvalidate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    serializer2 = ArticleSerializer(instance=article, data=serializer.data)
    if serializer2.is_valid():
        serializer2.validated_data['validated'] = False
        serializer2.save()
    return Response(serializer2.data)

@api_view(['GET'])
def editionsList(request):
    editions = Edition.objects.all()
    serializer = EditionSerializer(editions, many=True)
    return Response(serializer.data)
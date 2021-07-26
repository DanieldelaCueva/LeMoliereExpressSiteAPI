from .serializers import ArticleSerializer
from .models import Article
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import wget
import os
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articleList(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def articleDetail(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)

@login_required
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():

        url = serializer.validated_data['img_url']
        img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/media'
        wget.download(url,out = img_path)
        system_path = os.path.join(img_path, os.path.split(url)[1])
        init_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        relative_path = os.path.relpath(system_path, init_path)

        serializer.validated_data['img_url'] = relative_path

        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Not registered")

@login_required
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def articleUpdate(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=articles, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Not registered")

@login_required
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def articleDelete(request, pk):
    articles = Article.objects.get(id=pk)
    articles.delete()
    return Response('Successfully deleted')


@login_required
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def articleValidate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    serializer2 = ArticleSerializer(instance=article, data=serializer.data)
    if serializer2.is_valid():
        serializer2.validated_data['validated'] = True
        serializer2.save()
    return Response(serializer2.data)

@login_required
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def articleInvalidate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    serializer2 = ArticleSerializer(instance=article, data=serializer.data)
    if serializer2.is_valid():
        serializer2.validated_data['validated'] = False
        serializer2.save()
    return Response(serializer2.data)
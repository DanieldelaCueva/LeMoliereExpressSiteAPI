from rest_framework import serializers
from .models import Article, Edition

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['title', 'date', 'author', 'creator', 'group', 'img_url', 'content', 'language', 'validated']
        fields = '__all__'

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'

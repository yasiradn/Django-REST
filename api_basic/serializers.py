from rest_framework import serializers
from .models import Article


class ArticleSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']


from rest_framework import serializers
from crawler.models import Article, Video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('source', )


class ArticleSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'main_image', 'content', 'url', 'posted', 'videos')

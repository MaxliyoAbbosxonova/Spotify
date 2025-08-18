from rest_framework import serializers
from music.models import Content, Genre


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    # contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'

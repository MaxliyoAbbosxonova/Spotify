from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from music.models import Content, Genre
# from movie.models.movie import WatchedHistory, Genre, Content
# from movie.permissions import IsSuperUser
# from django.db.models import Q, Count, Sum
#
from music.serializers import GenreSerializer, ContentSerializer

# Create your views here.
@api_view(['GET','POST'])
def genre_list_or_create(request):
    if request.method == 'GET':
        genres=Genre.objects.all()
        search = request.query_params.get('search', None)
        if search:
            genres = genres.filter(name__icontains='search')
        serializer = GenreSerializer(genres, many=True)
        content = Content.objects.filter(genres__in=genres).count()
        return Response({
        "total_genres": genres.count(),
        "total_films": content,
        "genres": serializer.data},
        status=status.HTTP_200_OK)
    if  request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



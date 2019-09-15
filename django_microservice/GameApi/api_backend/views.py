from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from .serializers import GamesListSerializer
from .models import Game


# Create your views here.

class GamesListView(viewsets.ModelViewSet):
    parser_classes = (FileUploadParser,)

    def get_serializer_class(self):
        return GamesListSerializer

    def get_queryset(self):

        """
                Optionally restricts the returned gameslist to a given category_id,
                by filtering against a `category_id` query parameter in the URL.

        """
        queryset = Game.objects.all()
        category = self.request.query_params.get('category_id', None)
        if category is not None:
            queryset = queryset.filter(category__id=category)
        return queryset

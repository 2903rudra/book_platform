from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .services import fetch_books
from .models import *
from .serializers import *

class BookSearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        data = fetch_books(query)
        return Response(data, status=status.HTTP_200_OK)

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RecommendationListView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class LikeListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

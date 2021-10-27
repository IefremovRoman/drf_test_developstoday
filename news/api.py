from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer


class NewsListCreate(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsUpVote(APIView):
    def post(self, request, pk):
        get_object_or_404(News, pk=pk)
        News.objects.filter(pk=pk).update(upvotes=F("upvotes") + 1)
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(obj)
        return Response(serializer.data)


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Comment.objects.filter(news=pk)


class CommentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        news_pk = self.kwargs["news_pk"]
        return Comment.objects.filter(pk=pk, news=news_pk)

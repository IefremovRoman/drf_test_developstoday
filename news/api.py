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
    lookup_url_kwarg = "news_pk"


class NewsUpVote(APIView):
    lookup_url_kwarg = "news_pk"

    def post(self, request, news_pk):
        get_object_or_404(News, pk=news_pk)
        News.objects.filter(pk=news_pk).update(upvotes=F("upvotes") + 1)
        obj = get_object_or_404(News, pk=news_pk)
        serializer = NewsSerializer(obj)
        return Response(serializer.data)


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        news_pk = self.kwargs["news_pk"]
        return Comment.objects.filter(news=news_pk)

    def perform_create(self, serializer):
        serializer.save(news_id=self.kwargs["news_pk"])


class CommentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = "comment_pk"

    def get_queryset(self):
        news_pk = self.kwargs["news_pk"]
        return Comment.objects.filter(news=news_pk)

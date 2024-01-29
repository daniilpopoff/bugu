from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import generics
from .models import Topic, Quiz
from .serializers import TopicSerializer, QuizSerializer

class TopicListCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

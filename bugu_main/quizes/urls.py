# urls.py

from django.urls import path
from .views import TopicListCreateView, QuizListCreateView

urlpatterns = [
    path('topics/', TopicListCreateView.as_view(), name='topic-list-create'),
    path('quizes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    # Add more URL patterns as needed
]

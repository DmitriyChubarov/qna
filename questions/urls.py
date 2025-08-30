from django.urls import path
from .views import QuestionListView, QuestionDetailView
from answers.views import AnswerListView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<int:question_id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('<int:question_id>/answers/', AnswerListView.as_view(), name='answer-list'),
]
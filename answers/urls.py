from django.urls import path
from .views import AnswerDetailView

urlpatterns = [
    path('<int:answer_id>/', AnswerDetailView.as_view(), name='answer-detail'),
]
from django.db import models
from datetime import datetime
from questions.models import Question
import uuid

class Answer(models.Model):
    question_id: Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id: uuid.UUID = models.UUIDField(default=uuid.uuid4, editable=False)
    text: str = models.TextField(blank=False)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
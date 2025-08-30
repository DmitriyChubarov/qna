from django.db import models
from datetime import datetime

class Question(models.Model):
    text: str = models.TextField(blank=False)
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
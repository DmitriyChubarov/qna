from .models import Question
from django.db.models import QuerySet

class QuestionRepository:
    @staticmethod
    def create_question(text: str) -> Question:
        return Question.objects.create(text=text)

    @staticmethod
    def get_questions() -> QuerySet[Question]:
        return Question.objects.all()

    @staticmethod
    def get_question(question_id: int) -> Question:
        return Question.objects.get(id=question_id)

from .models import Question
from django.db.models import QuerySet

class QuestionRepository:
    def create_question(text: str) -> Question:
        return Question.objects.create(text=text)

    def get_questions() -> QuerySet[Question]:
        return Question.objects.all()

    def get_question(question_id: int) -> Question:
        return Question.objects.get(id=question_id)

    def delete_question(question_id: int) -> None:
        return Question.objects.get(id=question_id).delete()

from .models import Answer
from django.db.models import QuerySet
from questions.models import Question
from questions.repositories import QuestionRepository

class AnswerRepository:
    @staticmethod
    def create_answer(text: str, question_id: Question) -> Answer:
        question: Question = QuestionRepository.get_question(question_id)
        return Answer.objects.create(text=text, question_id=question)

    def get_answers(question_id: Question) -> list[Answer]:
        return Answer.objects.filter(question_id=question_id)
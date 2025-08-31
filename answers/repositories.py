from .models import Answer
from django.db.models import QuerySet
from questions.models import Question
from questions.repositories import QuestionRepository

class AnswerRepository:
    def create_answer(text: str, question_id: Question) -> Answer:
        question: Question = QuestionRepository.get_question(question_id)
        return Answer.objects.create(text=text, question_id=question)

    def get_answers(question_id: Question) -> list[Answer]:
        return Answer.objects.filter(question_id=question_id)

    def get_answer(answer_id: Answer) -> Answer:
        return Answer.objects.get(id=answer_id)
    
    def delete_answer(answer_id: Answer) -> None:
        return Answer.objects.get(id=answer_id).delete()
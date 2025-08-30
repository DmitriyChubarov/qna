from .models import Question
from .repositories import QuestionRepository
from django.core.exceptions import ObjectDoesNotExist

class QuestionService:
    @staticmethod
    def get_question_or_error(question_id: int) -> Question:
        try:
            return QuestionRepository.get_question(question_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Вопрос с ID {question_id} не найден")

    @staticmethod
    def get_questions_or_error() -> list[Question]:
        try:
            return QuestionRepository.get_questions()
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время получения запросов: {error}")

    @staticmethod
    def create_question_or_error(text: str) -> Question:
        try: 
            return QuestionRepository.create_question(text)
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время создания вопроса: {error}")
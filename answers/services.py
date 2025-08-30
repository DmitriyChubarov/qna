from .models import Answer
from .repositories import AnswerRepository
from django.core.exceptions import ObjectDoesNotExist
from questions.models import Question

class AnswerService:
    @staticmethod
    def create_answer_or_error(text: str, question_id: Question) -> Answer:
        try: 
            return AnswerRepository.create_answer(text, question_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Вопрос с ID {question_id} не найден_ тут объект не найден")
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время создания ответа: {error}")

    @staticmethod
    def get_answers_or_error(question_id: Question) -> list[Answer]:
        try:
            return AnswerRepository.get_answers(question_id)
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время получения ответов: {error}")

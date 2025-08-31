from .models import Answer
from .repositories import AnswerRepository
from django.core.exceptions import ObjectDoesNotExist
from questions.models import Question

class AnswerService:
    def create_answer_or_error(text: str, question_id: Question) -> Answer:
        try: 
            return AnswerRepository.create_answer(text, question_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Вопрос с ID {question_id} не найден_ тут объект не найден")
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время создания ответа: {error}")

    def get_answers_or_error(question_id: Question) -> list[Answer]:
        try:
            return AnswerRepository.get_answers(question_id)
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время получения ответов: {error}")

    def get_answer_or_error(answer_id: Answer) -> Answer:
        try:
            return AnswerRepository.get_answer(answer_id)
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время получения ответа: {error}")

    def delete_answer_or_error(answer_id: Answer) -> None:
        try:
            return AnswerRepository.delete_answer(answer_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Ответ с ID {answer_id} не найден")
        except Exception as error:
            raise ValueError(f"Произошла ошибка во время удаления ответа: {error}")
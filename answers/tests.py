from rest_framework.test import APITestCase
from rest_framework import status
from .models import Answer
from questions.models import Question
from qna.tests import TestCreate, TestGet, TestDelete

class QuestionTestCase(APITestCase, TestCreate, TestGet, TestDelete):

    def setUp(self):
        self.question = Question.objects.create(text="test question")
        self.answer = Answer.objects.create(text="test answer", question_id=self.question)

    def test_create_answer(self):
        self.main_test_create(f'/questions/{self.question.id}/answers/', Answer)

    def test_create_null_answer(self):
        self.main_test_create_null(f'/questions/{self.question.id}/answers/', Answer)

    def test_create_long_answer(self):
        self.main_test_create_long(f'/questions/{self.question.id}/answers/', Answer)

    def test_create_short_answer(self):
        self.main_test_create_short(f'/questions/{self.question.id}/answers/', Answer)

    def test_get_answer(self):
        self.main_test_get(f'/answers/{self.answer.id}/' , Answer)

    def test_get_null_answer(self):
        self.main_test_get_null(f'/answers/{self.answer.id + 1}/' , Answer)
    
    def test_delete_answer(self):
        self.main_test_delete(f'/answers/{self.answer.id}/', Answer)

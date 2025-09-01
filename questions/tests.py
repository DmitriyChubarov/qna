from rest_framework.test import APITestCase
from rest_framework import status
from .models import Question
from qna.tests import TestCreate, TestGet, TestDelete

class QuestionTestCase(APITestCase, TestCreate, TestGet, TestDelete):

    def setUp(self):
        self.question = Question.objects.create(text="test test")

    def test_create_question(self):
        self.main_test_сreate('/questions/', Question)

    def test_create_null_question(self):
        self.main_test_сreate_null('/questions/', Question)

    def test_create_long_question(self):
        self.main_test_сreate_long('/questions/', Question)

    def test_create_short_question(self):
        self.main_test_сreate_short('/questions/', Question)

    def test_get_all_question(self):
        self.main_test_get_all('/questions/', Question)

    def test_get_question(self):
        self.main_test_get(f'/questions/{self.question.id}/', Question)

    def test_get_null_question(self):
        self.main_test_get_null(f'/questions/{self.question.id + 1}/', Question)
    
    def test_delete_question(self):
        self.main_test_delete(f'/questions/{self.question.id}/', Question)



        
        



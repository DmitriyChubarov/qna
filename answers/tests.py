from rest_framework.test import APITestCase
from rest_framework import status
from .models import Answer
from questions.models import Question

class AnswersTestCase(APITestCase):

    def setUp(self):
        self.question = Question.objects.create(text="test question")
        self.answer = Answer.objects.create(text="test answer", question_id=self.question)

    def test_create_answer(self):
        url = f'/questions/{self.question.id}/answers/'
        data = {'text': 'test answer_2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 2)
        self.assertEqual(Answer.objects.filter(text='test answer_2').count(), 1)

    def test_get_answer(self):
        url = f'/answers/{self.answer.id}/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'test answer')

    def test_delete_answer(self):
        url = f'/answers/{self.answer.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Answer.objects.count(), 0)
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Question

class QuestionTestCase(APITestCase):

    def setUp(self):
        self.question = Question.objects.create(text="test question")

    def test_create_question(self):
        url = '/questions/'
        data = {'text': 'test question_2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Question.objects.filter(text='test question_2').count(), 1)

    def test_get_questions(self):
        url = '/questions/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['text'], 'test question')

    def test_get_question(self):
        url = f'/questions/{self.question.id}/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'test question')

    def test_delete_question(self):
        url = f'/questions/{self.question.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)
        
        



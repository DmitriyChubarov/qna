from rest_framework import status

class TestCreate:
    def check_create(self, url, model, text, status, count):
        response = self.client.post(url, {'text': text}, format='json')
        self.assertEqual(response.status_code, status)
        self.assertEqual(model.objects.count(), count)
        self.assertEqual(model.objects.filter(text=text).count(), count - 1)

    def main_test_сreate(self, url, model):
        self.check_create(url, model, 'correct test', status.HTTP_201_CREATED, 2)
        
    def main_test_сreate_null(self, url, model):
        self.check_create(url, model, '', status.HTTP_400_BAD_REQUEST, 1)

    def main_test_сreate_long(self, url, model):
        self.check_create(url, model, '1' * 1001, status.HTTP_400_BAD_REQUEST, 1)

    def main_test_сreate_short(self, url, model):
        self.check_create(url, model, '1234', status.HTTP_400_BAD_REQUEST, 1)

class TestGet:
    def check_get(self, url, model, status):
        response = self.client.get(url)
        self.assertEqual(response.status_code, status)

    def main_test_get(self, url, model):
        self.check_get(url, model, status.HTTP_200_OK)

    def main_test_get_null(self, url, model):
        self.check_get(url, model, status.HTTP_400_BAD_REQUEST)

    def main_test_get_all(self, url, model):
        self.check_get(url, model, status.HTTP_200_OK)

class TestDelete:
    def check_delete(self, url, model, status, count):
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status)
        self.assertEqual(model.objects.count(), count)

    def main_test_delete(self, url, model):
        self.check_delete(url, model, status.HTTP_204_NO_CONTENT, 0)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Answer
from .serializers import AnswerSerializer
from .services import AnswerService
from questions.models import Question

class AnswerListView(APIView):
    def post(self, request, question_id: Question) -> Response:
        serializer: AnswerSerializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            answer: Answer = AnswerService.create_answer_or_error(serializer.validated_data['text'], question_id)
        except ValueError as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(AnswerSerializer(answer).data, status=status.HTTP_201_CREATED)
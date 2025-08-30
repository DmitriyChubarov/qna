from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from .services import QuestionService
from answers.serializers import AnswerSerializer

class QuestionListView(APIView):
    def get(self, request) -> Response:
        try:
            questions: list[Question] = QuestionService.get_questions_or_error()
        except ValueError as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        serializer: QuestionSerializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer: QuestionSerializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            question: Question = QuestionService.create_question_or_error(serializer.validated_data['text'])
        except ValueError as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)

class QuestionDetailView(APIView):
    def get(self, request, question_id: int) -> Response:
        try:
            question: Question = QuestionService.get_question_or_error(question_id)
        except ValueError as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        serializer: QuestionSerializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
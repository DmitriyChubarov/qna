from rest_framework import serializers
from .models import Question
from answers.serializers import AnswerSerializer
from answers.services import AnswerService
from answers.models import Answer

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model= Question
        fields: list[str] = ['id', 'text', 'created_at', 'answers']
        read_only_fields: list[str] = ['id', 'created_at', 'answers']
    
    def get_answers(self, obj) -> list[Answer]:
        answers: list[Answer] = AnswerService.get_answers_or_error(obj.id)
        return AnswerSerializer(answers, many=True).data

    def validate_text(self, value) -> str:
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Минимальное количество символов - 5")
        if len(value.strip()) > 1000:
            raise serializers.ValidationError("Максимальное количество символов - 1000")
        return value

    
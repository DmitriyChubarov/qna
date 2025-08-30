from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Answer
        fields: list[str] = ['id', 'text', 'created_at', 'question_id', 'user_id']
        read_only_fields: list[str] = ['id', 'created_at', 'question_id', 'user_id']

    def validate_text(self, value) -> str:
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Минимальное количество символов - 5")
        if len(value.strip()) > 1000:
            raise serializers.ValidationError("Максимальное количество символов - 1000")
        return value

    
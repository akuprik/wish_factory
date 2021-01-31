from rest_framework import serializers

from .models import Poll, Question, AnswerVariant, Answer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('pk', 'name',
                  'start_date', 'stop_date',
                  'description',
                  )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question_type', 'poll', 'question_text')


class AnswerVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ('pk', 'question', 'text')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'poll_user', 'question', 'answer')


class UserPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('pk', 'name',
                  'description',
                  'questions',
                  )


class UserQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'pk',
            'question_type',
            'poll',
            'question_text',
            'answer_variants',
        )


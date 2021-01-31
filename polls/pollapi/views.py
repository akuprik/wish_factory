import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Poll, Question, AnswerVariant, Answer
from .serializers import (PollSerializer,
                          QuestionSerializer,
                          AnswerVariantSerializer,
                          AnswerSerializer,
                          UserPollSerializer,
                          UserQuestionsSerializer,
                          )


class PollViewSet(viewsets.ModelViewSet):
    """
    Для работы с опросом (чтение, создание редактирование, удаление)
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        """
        добавим новый опрос
        PUT detail только корректирует существующий
        """
        if self.kwargs.get('pk'):
            self.perform_update(serializer)
        else:
            serializer.save()


    def perform_update(self, serializer):
        """
        Отредактируем опрос
        при сохранении start_date не меняем
        """
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        print(poll.pk)
        serializer.save(start_date=poll.start_date)


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Для работы с вопросами
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class AnswerVariantViewSet(viewsets.ModelViewSet):
    """
    Для работы с вариантами ответов
    """
    queryset = AnswerVariant.objects.all()
    serializer_class = AnswerVariantSerializer
    permission_classes = [IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    """
    Для работы с ответами
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class UserPollViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Для выдачи пользователю списка опросов
    """
    queryset = Poll.objects.filter(start_date__lte=datetime.datetime.today()).\
        filter(stop_date__gte=datetime.datetime.today())
    serializer_class = UserPollSerializer


class UserQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Для выдачи пользователю вопроса
    """
    queryset = Question.objects.filter(poll__in=
        Poll.objects.filter(start_date__lte=datetime.datetime.today()).\
        filter(stop_date__gte=datetime.datetime.today()))
    serializer_class = UserQuestionsSerializer


class UserAnswerVariantViewSet(viewsets.ReadOnlyModelViewSet):
    """"
    Дя выдачи пользователю вариантов ответов на вопросы
    """
    queryset = AnswerVariant.objects.filter(
        question__in=Question.objects.filter(
            poll__in=Poll.objects.filter(
                start_date__lte=datetime.datetime.today()). \
                filter(stop_date__gte=datetime.datetime.today())
            )
        )
    serializer_class = AnswerVariantSerializer




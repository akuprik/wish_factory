from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Poll, Question, AnswerVariant, Answer
from .serializers import (PollSerializer,
                          QuestionSerializer,
                          AnswerVariantSerializer,
                          AnswerSerializer
                          )


class PollViewSet(viewsets.ModelViewSet):
    """
    Для работы с опросом (чтение, создание редактирование, удаление)
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    #filter_backends = [DjangoFilterBackend, ]
    #filterset_fields = ['group', ]


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


class AnswerVariantViewSet(viewsets.ModelViewSet):
    """
    Для работы с вариантами ответов
    """
    queryset = AnswerVariant.objects.all()
    serializer_class = AnswerVariantSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    Для работы с ответами
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


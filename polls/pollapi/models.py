from django.db import models


class PollUser(models.Model):
    """
    Пользователи, которые отвечают на опрос
    """
    name = models.CharField(max_length=255)


class Poll(models.Model):
    """
    Опрос
    """
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    stop_date = models.DateField()
    description = models.TextField()


class Question(models.Model):
    """
    Вопрос, может требовать текстовый ответ, выбор из вариантов,
    множественный выбор
    """
    QT_TEXT = 'tx'
    QT_SELECT = 'se'
    QT_MULTI_SELECT = 'ms'

    QUESTION_TYPE_CHOICES = [
        (QT_TEXT, 'text'),
        (QT_SELECT, 'select'),
        (QT_MULTI_SELECT, 'multi select'),
    ]
    question_type = models.CharField(max_length=2,
                                     choices=QUESTION_TYPE_CHOICES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,
                             related_name='questions')
    question_text = models.TextField()


class AnswerVariant(models.Model):
    """
    Вариант ответа на выбор
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answer_variants')
    text = models.TextField()


class Answer(models.Model):
    """
    Ответ пользователя на вопрос
    поле answer содержит текстовый ответ если QT_TEXT
    или pk варианта ответа для QT_SELECT и QT_MULTI_SELECT
    """
    poll_user = models.ForeignKey(PollUser, on_delete=models.CASCADE,
                                  related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers')
    answer = models.TextField()


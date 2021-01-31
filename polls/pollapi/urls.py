from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (PollViewSet,
                    QuestionViewSet,
                    AnswerVariantViewSet,
                    AnswerViewSet,
                    UserPollViewSet,
                    UserQuestionViewSet,
                    UserAnswerVariantViewSet,
                    )

router = DefaultRouter()

router.register('adm/poll', PollViewSet)
router.register('adm/question', QuestionViewSet)
router.register('adm/a-variant', AnswerVariantViewSet)
router.register('adm/answer', AnswerViewSet)
router.register('polls', UserPollViewSet)
router.register('questions', UserQuestionViewSet)
router.register('a-variants', UserAnswerVariantViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]

for item in router.urls:
    print(item)

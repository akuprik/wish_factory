from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (PollViewSet,
                    QuestionViewSet,
                    AnswerVariantViewSet,
                    AnswerViewSet,
                    )

router = DefaultRouter()

router.register('poll', PollViewSet)
router.register('question', QuestionViewSet)
router.register('a-variant', AnswerVariantViewSet)
router.register('answer', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]

for item in router.urls:
    print(item)

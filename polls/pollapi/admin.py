from django.contrib import admin
from .models import PollUser, Poll, Question, AnswerVariant, Answer


class PollUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('pk', 'name')


class PollAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'start_date', 'stop_date', 'description')
    search_fields = ('name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'poll', 'question_type', 'question_text')


class AnswerVariantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'text')
    search_fields = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'poll_user', 'question', 'answer')
    search_fields = ('poll_user', 'question')


admin.site.register(PollUser, PollUserAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerVariant, AnswerVariantAdmin)
admin.site.register(Answer, AnswerAdmin)

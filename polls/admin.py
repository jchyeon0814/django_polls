from django.contrib import admin

from .models import Question
from .models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}) # Date information - 그룹화, pub_date - 입력/수정할 필드
    ]
    
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    inlines = [ChoiceInline]
    
    list_filter = ['pub_date'] #필터 기능 활성화(pub_date 기준)
    search_fields = ['question_text'] #검색 창 표시(검색 기준은 qeustion_text)
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


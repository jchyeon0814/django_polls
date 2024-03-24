import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date' #정렬 기준 값 설정(메서드에 의한 값 정렬은 불가능하며 대신 다른 정렬 기준(pub_date)을 사용하도록 설정)
    was_published_recently.boolean = True #불리언 값 형태일 경우 아이콘으로 표시
    was_published_recently.short_description = 'Published recently?' #항목의 헤더 이름 설정
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
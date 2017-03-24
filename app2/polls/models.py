from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model): # 항상 Model 클래스를 상속받는다
    #pk 는 자동으로 생성
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "최근 1일 안에 작성되었나?"

class Choice(models.Model):
    # 질문을 삭제 했을 떄 연관 항목을 어떻게 할지 설정 - 자동 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

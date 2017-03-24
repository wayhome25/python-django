from django.db import models
# from django.utils import timezone
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model): #슈퍼클래스 models의 하위클래스 Model을 상속받는다.
    # 필요한 데이터 정의
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default = 5)
    update_date = models.DateTimeField()

    # 로또 번호 생성 및 데이터베이스 저장
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46)) #[1, 2, 3.....44, 45]
        for _ in range(0, self.num_lotto): # self.num_lotto 수만큼 반복해서 아래를 수행한다.
            random.shuffle(origin) # origin 리스트 순서를 섞는다.
            guess = origin[:6] #index번호 0부터 5 까지를 뽑아낸다.
            guess.sort()
            self.lottos += str(guess) + '\n'
        # self.update_date = timezone.now()
        self.update_date = timezone.now()
        self.save() # 오브젝트를 db에 저장

    def __str__(self):
        return '%s - %s' % (self.name, self.text)

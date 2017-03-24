from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos = GuessNumbers.objects.all().order_by('-update_date') #shell에서 하는 것 처럼 데이터를 읽어온다.
    return render(request, 'lotto/default.html', {'lottos': lottos}) # 템플릿 파일 경로 지정, 데이터 전달

def post(request):
    if request.method == "POST":
         # create a form instance and populate it with data from the request:
        form = PostForm(request.POST) #PostForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            lotto = form.save(commit = False) #lotto 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
            lotto.generate()
            return redirect('lotto:index') #url의 name을 경로대신 입력한다.
    else:
        form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'lotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달

def detail(request, lottokey): # perameter 'lottokey'를 함께 전달
    lotto = GuessNumbers.objects.get(pk = lottokey) #primary key가 lottokey 파라미터와 일치하는 오브젝트를 가져온다.
    return render(request, 'lotto/detail.html', {'lotto' : lotto})

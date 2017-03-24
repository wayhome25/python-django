from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Question, Choice

# Class-based views - generic view 활용
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self): # 오버라이딩
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     # 모델클래스 Question을 가져온다. (pub_date 내림차순으로)
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html',{'latest_question_list' : latest_question_list})

# url을 views 의 메소드들과 연결해주는 것 >> function based view

# def detail(request, question_id):
#     q = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/detail.html', {'question' : q})
#
# def results(request, question_id): #question_id를 파라미터로 받는다.
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id): #POST를 처리할 수 있도록 작성한다.
    question = get_object_or_404(Question, pk = question_id)
    try:
        # POST form에서 'choice' 이름 값을 갖는 input의 value 값을 가져온다.
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # return redirect('polls:results', question_id = question.id)
        return redirect('polls:results', pk = question.id) # class-based view

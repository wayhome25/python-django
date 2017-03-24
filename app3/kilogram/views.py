from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
from .forms import CreateUserForm # 장고의 기본 회원가입 폼을 커스터마이징 한 폼
from django.core.urlresolvers import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.



class IndexView(TemplateView):
    template_name = 'kilogram/index.html'


# CBV (Class Based View 작성!)
class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

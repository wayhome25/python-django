# polls - urls.py

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'polls' #url 네임 스페이스

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     # 숫자로 이루어진 question_id를 매개변수로 views.py에 넘긴다
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^about/$', TemplateView.as_view(template_name="polls/about.html"))
]

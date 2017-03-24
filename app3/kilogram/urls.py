from django.conf.urls import url
from . import views

app_name = 'kilogram' # url 네임스페이스 설정

urlpatterns = [
    # 제네릭 뷰를 사용하여 url을 처리한다
    url(r'^$', views.IndexView.as_view(), name = 'index'),
]

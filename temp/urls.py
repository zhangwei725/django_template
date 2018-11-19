from django.conf.urls import url

from temp import views

urlpatterns = [
    url('base/', views.base),
    # 通过函数或者索引名来反向生成路径
    url('login1/', views.login, name='login'),
    url(r'list/(\d+)/(\d+)/', views.list, name='list'),
    url(r'kw/(?P<id>\d+)/', views.kw, name='kw'),
    url(r'1/', views.test1),
]

import datetime

from django.shortcuts import render
from django.urls import reverse


class User:
    pass


# ctrl + alt +l
def base(request):
    # 基本类型
    msg = '您输入的密码有误'
    number = 2

    # 复杂类型
    li = [3, 4, 3, 4]
    # dic = {'name': '娇娇', 'age': 18}

    test = User()
    # 动态添加属性
    test.name = '空空'
    test.age = 38
    # {'msg': msg, 'li': li}

    nav = ['首页', '电脑', '服装']

    return render(request, 'temp.html', locals())


def login(request):
    username = request.GET.get('username')
    if username == 'zhangsan':
        pass
        # 登录成功
    else:
        return render(request, 'temp.html', {'msg': '账号密码错误'})
        # 登录失败


def list(request, page, size):
    return None


def kw(request, id):
    # 重定向使用
    reverse('list', args=[1, 10])  # list/1/10/
    return None


def test1(request):
    now = datetime.datetime.now()
    return render(request, 'child.html', locals())

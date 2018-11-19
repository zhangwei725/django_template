from django import template

# 实例化注册器
register = template.Library()


@register.filter
def test1(value, number):
    # 一定要要有返回值
    return value * number


@register.filter
def test2(value, n1, n2):
    # 一定要要有返回值
    return value * n1 * n2


@register.simple_tag
def test_tags(n, n1, n2):
    # 一定要要有返回值
    return n * n1 * n2

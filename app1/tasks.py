# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 下午12:46
# @Author  : zhongxin
# @Email   : 490336534@qq.com
# @File    : tasks.py
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

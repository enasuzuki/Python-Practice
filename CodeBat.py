#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:03:00 2020

@author: ena
"""


#def-1
def hello():  # def + function name + ():
    print("Hello")  #transaction


hello()  #call the function


def ena():
    print("Ena")


ena()


#def-2
def add(a, b):
    return (a + b)


x = add(3, 4)
print(x)


def devide(c, d):
    return (c / d)


y = devide(30, 6)
print(y)


def print_add(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("a + b + c = ", a + b + c)


print_add(1, 4, 6)  #in the order of a,b,c
print_add(1, c=10, b=5)  #you can decide the order


def print_add_default(a, b, c=100):  #you can set default
    print("a = ", a)
    print("b = ", b)
    print("c= ", c)
    print("a + b + c = ", a + b + c)


print_add_default(5, 13)


#def-3　＊args
def func_args(*args):  #＊をつけると何個でも呼び出し可能
    print(args)


func_args(1, 10)
func_args(1, 2, 3, 4, 5)


#def-3 *kwargs
def func_kwargs(**kwargs):  #＊＊をつけると辞書として受け取る
    print(kwargs)


func_kwargs(a=1, b=10)
func_kwargs(c=90, d=100, e=70)


#def-4 return
def func_return(a, b):
    return (a + b)


x = func_return(3, 4)
print(x)
print(type(x))


def func_return_multi(a, b):
    return [a + b, a * b, a / b]  #[]で囲むとリスト


y = func_return_multi(1, 2)
print(y)
print(type(y))
"""
CodingBad
"""


#warmup-1
#near_hundred
def near_hundred(n):
    if (n <= 110 and n >= 90) or (n <= 210 and n >= 190):
        return (True)
    else:
        return (False)


#pos_neg
def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


#front3
def front3(str):
    if len(str) >= 3:
        return (str[:3] * 3)
    else:
        return (str * 3)


#missing_char !!!
def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return (front + back)


#front_back
def front_back(str):
    if len(str) >= 2:
        front = str[0]
        back = str[len(str) - 1]
        middle = str[1:-1]
        return (back + middle + front)


#not_strnig !!!
def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return (str)
    else:
        return ("not " + str)

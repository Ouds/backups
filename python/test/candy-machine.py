#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#===============================================================================
# Title: 模拟糖果机
# Author: 某某某
# Date: 2020-10-20
#===============================================================================

'''
Write a program that simulates a candy machine. A candy bar is $2.00, and the program should continue to ask the user for money until they have 'deposited' at least $2.00. Your program should follow the sample output as closely as possible. User input is in red. 
>>> $2.00 left to pay. How much are you paying? 0.25 
>>> $1.75 left to pay. How much are you paying? 0.50 
>>> $1.50 left to pay. How much are you paying? 0.39 
>>> $1.11 left to pay. How much are you paying? 2 
>>> Here is your candy bar. 

编写一个模拟糖果机的程序。 糖果是2.00美元，程序应继续向用户询问钱，直到他们“存款”至少2.00美元。 您的程序应尽可能接近示例输出。 用户输入为红色。
>>>还剩$ 2.00。 您要付多少钱？ 剩下的0.25 
>>> $ 1.75。 您要付多少钱？ 还剩下0.50 
>>> 1.50美元。 您要付多少钱？ 0.39 
>>>剩下的$ 1.11。 您要付多少钱？ 2 
>>>这是您的糖果吧。
'''

def balance(candy_money, payment):
    balance = payment - candy_money

    if balance < 0:
        candy_money = abs(balance)
        pay(candy_money)
    else:
        print('Here is your candy bar.')
        sys.exit()

def pay(candy_money):
    payment = float(input('${:.2f} left to pay. How much are you paying? '.format(candy_money)))
    balance(candy_money, payment)

if __name__ == "__main__":
    import sys
    
    candy_money = 2.00
    pay(candy_money)


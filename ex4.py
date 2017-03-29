#!/usr/bin/python
# -*- coding: utf-8 -*-

#5.1占有的内存不一样

#5.2
# (a)
def time_xy(x,y):
	return x*y
#(b)
print time_xy(6,7)

#5.3

def grade(score):
	if score>90:
		print "A"
	elif score>80:
		print 'B'
	elif score>70:
		print 'C'
	elif score>60:
		print 'D'
	else:
		print 'F'

#5.4

def is_leapyear(year):
	if (year % 4==0 and year % 100 != 0) or year % 400:
		print "%d is leap year"% year
print is_leapyear(1985),is_leapyear(1900)
		
#5.5

def max_num(num):
	a=num/10 # 10美分数量
	b=int((num % 10)/5) #5美分数量
	c=int(num-a*10-b*5) # 1美分数量
	return a+b+c
print max_num(76),max_num(58)

#5.6 不清楚题意

#5.7
def profit_tax(profit):
	if profit>10000000:
		return profit*0.3
	elif profit>5000000:
		return profit*0.2
	else:
		return profit*0.1
		
#5.8 
#(a)
def area_squre(num):
	return num*num

def volume_cube(num):
	return num*num*num
	
import math
#(b)
def area_circle(num):
	return float(math.pi*num*num)

def volume_sphere(num):
	return float(4*math.pi*num*num*num/3)

#5.9可能版本问题，笔者按题目代码却出错

#5.10

def tran(f_degree):
	return (f_degree-32)*float(5/9)
	
#5.11
x=[x for x in range(1,20) if x % 2 ==0]
x=[x for x in range(1,2o) if x % 2]

#5.12 可自行练习.可按下面方式不断尝试
12**10

#5.13

def minitue-h(minute,hour):
	return minute+60*minute

#5.14

def profit(rate):
	return float((1+rate)**365-1) # 一年按365天，rate是每天的利息

#5.15 
 def mutiple_divisor(n,m):
	if n>m:
		if n % m:
			return n*m,1
		else:
			return n,m
	else:
		if m % n:
			return n*m,1
		else:
			return m,1

#5.16

def deposit(n,m):
	n=raw_input('Enter opening balance:')
	m=raw_input('Enter monthly money:')
	k=0
	print 'Amount Remaining'
	print 'Pamt_no','Paid','Balance'
	while n:
		k=k+1
		n=n-m * k
		print k,'''$'''+m,'''$'''+n

#5.17
import random

def order(num):
	for i in range(len(num)-1):
		for j in range(1,len(num)):
			if i<=j and num[i]<=num[j]:
				num[i],num[j]=num[j],num[i]
				
	return num

L=[]
N=int(raw_input('Enter a num between 1~100；'))
while N:
	L.append(random.uniform(0,231))
	N=N-1

print order(L)
	
	


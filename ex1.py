#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2.1 变量 
str='ABC'
num=13
num
str
print str
print num
print '%s' %str
print '%d'%num

#2.2 运算
#(a)验证加减乘除
#(b)9
#(c)不一样，运行脚本的话，无返回值
#(d)程序返回9，运行脚本，无返回值
#(e)按下面方法改进
print 1+2*4 

#2.3 自己练习即可

#2.4数值和操作符
#(a)
str2=raw_input('Enter the str:')
print str2
#(b)
num2=raw_input('Enter the num:')
print int(num)

#2.5循环和数字
#(a)
b=[0,1,2,3,4,5,6,7,8,9,10]
j=0

#for 循环
for i in b:
    print i
#while 循环
while j<len(b):
    print b[j]
    j=j+1
    
#(b)
#for 循环
for i in range(11):
    print i

#while 循环
b=[i for  i in range(11)]
while j<len(b):
    print b[j]
    j=j+1

#2.6条件判断

def neg_pos(num):
    if num>0:
        print '%d is positeve num'%num
    elif num<0:
        print '%d is negitive num'%num
    else:
        print '%d must be zero'% 0


        
def neg_pos1(num):
    num=int(raw_input('Enter the num'))
    if num>0:
        print '%d is positeve num'%num
    elif num<0:
        print '%d is negitive num'%num
    else:
        print '%d must be zero'% 0

#2.7 循环和字串
a="abc"
i=0

#while 循环
while i <len(a):
	print a[i]
	i=i+1
	
#for 循环
for j in a:
	print j 

#2.8循环和操作符
a=[1,3,5,2,6]
i=0
sum=0

#while 循环
while i<len(a):
	sum=sum+a[i]
	i=i+1
	
print sum
sum=0
#for 循环
for j in a:
	sum=sum+j
	
print sum

#2.9循环和操作符
a=[1,3,5,2,6]
i=0
sum=0.0

#while 循环
while i<len(a):
	sum=sum+a[i]
	i=i+1
	
print sum/len(a)

sum=0.0
#for 循环
for j in a:
	sum=sum+j
	
print sum/len(a)

#2.10带循环和判断条件的用户输入
a=int(raw_input('Enter a num between 1 to 100:'))
if 1<a<100:
	print a
else:
	while a>100 or a<1:
		a=int(raw_input('Enter again:'))
		if 1<a<100:
			print a
		
#2.11写一个带文本菜单的程序

class Menu(object):

	def __init__(self,score):
		self.score=score
		
	def sum_num(self):
		sum=0.0
		for i in self.score:
			sum=sum+i
		return sum
	def ave_num(self):
		sum=0.0
		for i in self.score:
			sum=sum+i
		return sum/len(self.score)
		

a=Menu([1,2,3,4,5,6])
print a.sum_num()
print a.ave_num()
#2.12,2.13 自行练习

#2.14 操作符优先级和括号分组


print -2*(4+3)*2

#2.15 元素排序

def order_up(num):
	for i in range(0,len(num)-1):
		for j in range(i,len(num)):
			if num[i]>num[j]:
				num[i],num[j]=num[j],num[i]
	return num

def order_down(num):
	for i in range(0,len(num)-1):
		for j in range(i,len(num)):
			if num[i]<num[j]:
				num[i],num[j]=num[j],num[i]
	return num	
	
				
print order_up([1,3,2,4,5,9,6,7])

print order_down([1,3,2,4,5,9,6,7])
#2.16 运行2.15代码


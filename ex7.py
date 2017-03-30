#!/usr/bin/env python
# -*- coding: utf-8 -*-

#8.1

#8.2

def fti():
    f=int(input('Enter start num:'))
    t=int(input('Enter end num:'))
    i=int(input('Enter increment:'))
    for k in range(f,t+1,i):
        print (k)

fti()

#8.3

for i in range(10):
    print(i)

for k in range(3,19,3):
    print(k)
for j in range(-20,861,220):
    print(j)

#8.4

def is_premier(num):
    count=int(num/2)
    while count>0:
        if num % count ==0:
            m=count
            break
        count=count-1
    if m==1:
        # print(num, 'is premier')
        #print(m)
        return True
    else:
        # print(num,'is not premier')
        # print(m)
        return False
print(is_premier(15))
print(is_premier(13))

#8.5

def get_factor(num):
    #count=int(num/2)
    count=num
    while num>0:
         if count % num ==0:
             print(num)
         num=num-1
get_factor(15)

#8.7

def is_perfect(num):
    count=int(num/2)
    sum=0
    while count>0:
        if num % count ==0:
            sum+=count
        count=count-1
    if sum==num:
        return True
    else:
        return False
print(is_perfect(6))
print(is_perfect(7))

#8.8
def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    return fact

print(factorial(5))

#8.9

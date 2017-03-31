#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 6.1 有，用in，not...in

#6.2

#6.3
def order(num):
	for i in range(len(num)-1):
		for j in range(i,len(num)):
			if num[i]<num[j]:
				num[i],num[j]=num[j],num[i]
	
	return num

print order([1,7,9,2,3])

#6.4 

def grade(score):
	if score>90:
		return "A"
	elif score>80:
		return 'B'
	elif score>70:
		return 'C'
	elif score>60:
		return 'D'
	else:
		return 'F'

def grade_list(list):
	L=[]
	k=0
	for i in list:
		k=k+i
		L.append(grade(i))
	return L,float(k/len(list))

print grade_list([89,76,90,75,67])

#6.5
# (a)
str1='abcdef'
for i in range(len(str1)):
	if i==0:
		print str1[i],str1[i+1]
	elif i==len(str1)-1 :
		print str1[i-1],str1[i]
	else:
		print str1[i-1],str1[i],str1[i+1]

#(b)
'''	
def same_str(str1,str2):
	i,j=len(str1),len(str2)
	str3=''
	if i!=j:
		print '%s is not same as %s'%(str1,str2)
	else:
		str3=str1+str2
		if str3==str1*2:
			print '%s is  same as %s'%(str1,str2)	
		else:
			print '%s is not same as %s'%(str1,str2)	
same_str("abc","cde")
same_str("abc","abc")
'''
def same_char(str1,str2):
	str3=str1+str2
	if str3==str1*2:
		print '%s is  same as %s'%(str1,str2)	
	else:
		print '%s is not same as %s'%(str1,str2)	
same_char('afr','cde')
same_char('bcd','bcd')		

#(c)

def repeat_char(char):
	for i in range(len(char)-1):
		for j in range(i+1,len(char)):
			if char[i]==char[j]:
				print '% d char is same as %d char'%(i+1,j+1)

repeat_char('abcdadb')

def chiasmus(char):
	i=len(char)
	char1=char
	for k in range(i-1):
		char1=char1+char[-k-2]
	return char1
print chiasmus('abcdf')	
#6.6

def delete_space(list1):
	l=0
	r=len(list1)-1
	while list1[l]==' ':
		l=1
	while list1[r]==' ':
		r=r-1
	return list1[l:r+1]

print delete_space(' abc '),delete_space(' abc'),delete_space('abc ')


#6.7 没看到例6.5

#6.8

d={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}

def number_char(num):
	char1=str(num)
	char2=''	
	i=len(char1)
	for k in range(i):
		char2=char2+d[char1[k]]
		if k<i-1:
			char2=char2+'-'
		
	return char2
print number_char(12347)	

#6.9 

def transfomate():
    global hour,minute
    row_time = raw_input('输入你要转换的时间(格式H:M-->  xx:yy)：')
    time_list = row_time.split(':')
    hour = time_list[0]
    minute = time_list[1]
    total = int(hour) * 60 + int(minute)
    return '转换为分钟---->' + str(total)
 
print transfomate()
   
     
def m_trans_h():
    get_time = int(raw_input('输入你要转换的时间(分钟数-->一个正整数):'))
    hour = get_time / 60
    minute = get_time % 60 
    print hour,'H',':',minute,'M'
     
m_trans_h()

#6.10

str_1 = raw_input('Enter your string:')
str_list = list(str_1)
result_list = []
for i in str_list:
    if i.isupper():
        result_list.append(i.lower())
    elif i.islower():
        result_list.append(i.upper())
    else:
        result_list.append(i)
 
result = ''.join(result_list)
print 'Before: %s' % str_1
print 'After: %s' % result

#6.11

#(a)
print '--------------(a)--------------'
def format_ip():
    num = raw_input('Enter ip number(12 integer)')
    w = num[0:3]
    x = num[3:6]
    y = num[6:9]
    z = num[9:12]
    tmp = [w,x,y,z]
    ip = '.'.join(tmp)
    return ip
 
if __name__ == '__main__':
    print format_ip()
     
 
#(b)
print '--------------(b)--------------'
def re_format_ip():
    ip = raw_input('Enter ip:')
    tmp = ip.split('.')
    num = ''.join(tmp) 
    return num
if __name__ == '__main__':
    print re_format_ip()



#Reading dict from user
'''n=int(input())
d={}
for i in range(0,n):
    key,value=map(int,input().split())
    d[key]=value
print(d)'''

#
'''hr=int(input())
min=int(input())
total=hr *60+60+min*60
print(total)'''


#
'''secs=int(input())
min=int(input())
a=secs//3600
b=min%60
print(a)
print(b)'''

#
sec=10000
h = sec//3600
min_sec =sec-h*3600
min = min_sec//60
s=min_sec-min*60
print(h,min,s)

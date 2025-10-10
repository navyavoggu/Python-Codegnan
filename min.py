#min element
'''lst = [2,5,6,3,9]
for i in lst:
    print(min(lst))'''

#SUM ELEMENT
'''s=0
lst = [11,12,13,14,15]
for num in lst:
    s = s+num
    print(s)'''
#product element
'''s=1
lst = [11,12,13,14,15]
for num in lst:
    s = s*num
    print(s)'''


#max element
lst = [1,5,4,3]
max_val = lst[0]
for i in range(1,len(lst)):
  if max_val<lst[i]:
     max_val = lst[i]
  print(max_val)

#find reverse of a number
'''n = 456
res = 0
while n>0:
    rem = n%10
    n = n // 10
    res = res * 10 + rem
    print(res)'''

#find the even and odd
'''import math
lst = [2,4,5,1]
res =[]
for num in lst:
  if num % 2 ==0:
       res.append(num * num)
  else:
      res.append(math.sqrt(num))
print(res)'''


    


    

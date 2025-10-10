#lst = [10,5,6,4]
'''n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 % 2 ==0:
    print("even")
else:
    print("odd")
if n2 % 2 ==0:
     print("even")
else:
     print("odd")
if n3 % 2 ==0:
    print("even")
else:
    print("odd")'''

#for statement
'''num = int(input())
for num in range(1,11):
    print(num,end = ' ')'''
    
#for else statement
'''num = int(input())
for num in range(1,11):
    print(num,end = ' ')
else:
    print("program done")'''
#even numbers between 1 -100
'''num = int(input())
for num in range(101):
  if num % 2 ==0:
      print(num,end = ' ')'''

#odd numbers between 1 -100
 
'''num = int(input())
for num in range(101):
  if num % 2 ==1:
      print(num,end = ' ')'''

#tables
'''n = int(input())
for i in range(1,11):
        print(f"{n} * {i} = {n*i}")'''

#list in even numbers
lst =list(map(int,input().split()))
res = []
for i in range(0,len(lst)):
    if lst[i] % 2 ==0:
        res.append(lst[i])
print(res)


  
     
     



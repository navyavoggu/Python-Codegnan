#count
'''n = int(input())
count = 0
while n>0:
    rem = n%10
    n = n // 10
    count+=1
print(count)'''

#armstrong number
#an armstrong numbers is number that is equal to sum of its own digits each raiswdto the
#power of the number of digits
'''n = int(input())
length = len(str(n))
temp1 =n
res=0
while n>0:
    rem = n%10
    
    res= res+ rem ** length
    n = n//10
    
if res == temp1:
    print(f"{temp1} is an Armstrong number.")
else:
    print(f"{temp1} is NOT an Armstrong number.")'''
##armstrong for loop
'''armstrong_list = []
for n in range(1,1001):
    length = len (str(n))
    temp =n
    res =0
    while 0<temp:
        rem = temp % 10
        res = res+ rem **length
        
    if res ==n:
        armstrong_list.append(n)
print(armstrong_list)'''

##patterns
'''n = int(input())
for i in range(n):
    for  j in range(n):
        print(j+1, end = ' ')
    print()'''


'''n = int(input())
for i in range(n):
    for  j in range(n):
        print(i+1, end = ' ')
    print()'''

'''n = int(input())
for i in range(n):
    for  j in range(n):
        print(i, end = ' ')
    print()'''
    
'''n = int(input())
for i in range(n):
    for  j in range(n):
        print("*", end = ' ')
    print()'''
##
'''n = int(input())
for i in range(n):
    for  j in range(n):
        print(i*n+j+1, end = ' ') 
    print()'''
##
n = chr(input())
for i in range(n):
    for  j in range(n):
        print(ord(value)+1, end = ' ') 
    print()


















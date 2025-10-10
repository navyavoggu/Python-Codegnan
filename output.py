#old style output formating-using comma
'''name = "Ravi"
age = 20
print("Name is",name,"and age is",age)'''

#modulo operator output formating
#Access specifiers
#%d- Integers
#%f - Float
#%s - String
'''name = "Ravi"
age = 20
print("Name is %s and age is %d"%(name,age))'''

#dot format
'''name = "Ravi"
age = 20
print("Name is {} and age is {}".format(name,age))
print("Name is {} and age is {}".format(age,name))
print("Name is {1} and age is {0}".format(name,age+5))'''

# f format
'''name = "Ravi"
age = 20
percentage = 95.2568
print(f"name is {name} and age is {age}")
print(f"name is {name} and age is {age} and i have {percentage:.2f}")
num = 10
print(f"{num:0{5}d}")
print(f"{num:{5}d}")'''

#eval() function
'''res= eval('52+3')
print(res)
print('52+3')
print(eval('53+3'))'''

#
'''num= eval(input())
print(type(num),num)'''

#
l=list(map(int,input().split()))
print(l)

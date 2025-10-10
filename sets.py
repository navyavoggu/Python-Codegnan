#read set of integred from user
'''s=set(map(int,input().split()))
print(s)'''

#set operations
'''s1={1,2,"HI","HELLO"}
s2={"python",'java'}
print("Union",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Difference:",s1.difference(s2))
print("Symmetric Difference:",s1.symmetric_difference(s2))
print("Subset:",s1.issubset(s2))
print("Superset:",s1.issuperset(s2))
print("Disjoint set:",s1.isdisjoint(s2))'''

#set operations
'''s1={1,2,5}
s2={1,3,4,5}
print("Union:",s1|s2)
print("Intersection:",s1&s2)
print("Difference:",s1-s2)
print("Symmetric Difference:",s1^s2)'''

#add()
#remove()
#discard()
#update()
s1={1,2,3.5,65,43}
s1.add(100)
s1.add(1)
print(s1)
s1.remove(100)
print(s1)
#s1.remove(100)#keyError
s1.discard(100)
s1.discard(2)
print(s1)
s1.update({1,2,3})
print(s1)

#example
#duplicate keys
'''d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:'Z'}
print(d)'''

#example
#dictonary 
'''d={"A":1,"Hi","Hello",(1,2,3):(10,20,30),12.241:10.00,'Z'}
print(d)'''

#values access by passing keys
'''d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:'Z'}
print(d[1])
print(d["A"])
#update values and items
d[1]="X"
print(d[1])
d['1']='x'
print(d['1'])
print(d)'''

#empty dictionary reprresntation
'''d1={}
d2=dict()
print(type(d1),type(d2))'''

#methods
'''-get(key,default)-It returns the values if key is present in dictionary,otherwise default value
-update(dict) - it updates the dictionary with new_dictionary items
-pop(key)- It return and removes the item,if key is persent in dictionary otherwise last KeyError
-popitem()-It return and removes the last item
-keys()-It returns the list of keys
-values()-It returns the list values
-items()-It returns the list of tuple of key value pairs
-clear()-It removes all items form dict.'''
##
'''d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:'Z'}
print(d.get(1))
print(d.get(10))
print(d.get(10,'Key not present'))
print(d.get(10,0))'''


##
'''d1= {"batch":39,"Course":"PFS"}
d2= {"Course":"JFS","lang":"java"}
d1.update(d2)
print(d1)'''

#popitem,clear()
d={'batch':39,'Course': 'PFS','lang':'Python'}
print(d.popitem())
print(d.pop('Course'))
print(d)
d.clear()
print(d)

#
t=(10,20,[1,2,3,4],30)
t[2].append(100)
print(t)
























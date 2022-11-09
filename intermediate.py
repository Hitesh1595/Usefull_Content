# list..........ordered ,mutable,allow duplicate element

mylist = [1,2,2.35]
# mylist.append('hit')

# insert......
mylist.insert(2,123)
# remove ......
mylist.remove(2)
# reverse ....
mylist.reverse()

# sort ......
mylist_str = ['ht','labana','kite']
mylist_str = sorted(mylist_str,key=len,reverse=True) # return a new list 

print(mylist_str.index('ht'))

# addition of list.......

list1 = [0]*5
list2 = [1]*3
print(list1 + list2)

# list compresion .....

list3 = [x*x for x in range(5)]
print(list3)

#..............................................................................--------------

# tuple: ordered,immutable,allows duplicate elements....

t_list = tuple(["hit",2])
print(type(t_list))
item = t_list[0]
print(item)

# dictionary : key : value,unordered,mutable

mydict = {'name':'hir','age':28,'lie':253,'hsss':'jas'}
print(mydict)
mydict1 = dict(name = 'hir',age = 12)
print(mydict1)
# deleting .......--------
del mydict['name']
mydict1.pop('name')

for key in mydict.keys():
    print(key,end = ' ')
for value in mydict.values():
    print(value,end = ' ')

for key,value in mydict.items():
    print(key,value)

# merge ..(overridden)
mydict.update(mydict1)
print(mydict)

# Sets : unordered,mutable,dublicates

s1 = {1,2,3,4,5,6}
s2 = set([1,2,3,4,5,6])
# print(s1)
# print(s2)

odds = {1,3,5,7,9}
even = {0,2,4,6,8}
prime = {2,3,5,7,11}

print(odds.union(even))
print(even.intersection(prime))

a = frozenset([1,2,3,3]) # cannot change after creation
print(a)

# String : ordered,immutable,text representation----------------------

s = '[1,2,3]'
b = 'hello world'
print(s)

a = s.strip('[]')
print((a))

# most impline ...........////////////////////////////////
print(list(map(int,a.split(','))))
##############################################
print(b.index('hello'))
print(b.find('o')) # if not then return -1
print(b.count('p'))

print(b.replace('world','india')) # return new string if ind else original string
a = 3.21
my_string =f"value of a is {a:.1f}"
print(my_string) 

# Collections:Counter,namedtuple,Orderedict,deffaultDict,dequeue....-----------

from collections import Counter

a = 'aaaaaaaabbbbbbddddggggggg'

count = Counter(a)

print(count.values())
print(count.keys())
print(count.items())
print(count)


print(count.most_common(2))

from collections import deque

d = deque()

for i in range(6):
    d.append(i)

print(d)

d.rotate(2)
print(d)
d.rotate(-1)
print(d)


# Itertools:product,permutations,combinations,accumulate,groupby,and infinite itterators


from itertools import product


a = [1,2]
b = [3,4]
prod = product(a,b) # other option ex repeat 
print(prod)
print(list(prod))

from itertools import permutations

a = [1,2,3]
per = permutations(a)
print(list(per))

from itertools import combinations

a = [1,2,3,4]
com = combinations(a,r = 2)
print(list(com))

from itertools import accumulate # sum in the list from left to right

a = [1,2,3,4]
acc = accumulate(a)
print(list(acc))

from itertools import groupby

# Lambda arguments : expressions

add2 = lambda x : x + 2

print(add2(5))

mul = lambda x,y: x*y
print(mul(5,3))

sort = [(1,2),(3,5),(-1,6),(8,-2)]

a = sorted(sort)
print(a)

b = sorted(sort,key = lambda x : x[1])
print(b)


# try except error-------------------------------------------------------
try:
    a = 5 /2
    b = 'c' + 'n'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('every thing is fine')

finally:
    print('cleaning up the code')

# json -----------------------------
import json
person = {'name':'hit','class': 123,'last':'lower','titles':['eng','btech'],'child':False}

pjson = json.dumps(person,indent=4,sort_keys=True)
# print(pjson)
# pyhton to json format
with open('person.json','w') as file:
    json.dump(person,file,indent=4)

# json to python
with open('person.json','r') as file:
    p = json.load(file)
    print(p)

# decorator --- adding some addition functionlity to the function

def last_name(func):

    def wrapper():
        print('hello')
        func()
        print('pratap')
    return wrapper
@last_name  # shortcut of decoorator
def print_name():
    print('hitesh')

# print_name = last_name(print_name)    long form of decorator

print_name()


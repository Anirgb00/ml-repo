
######python data structure

import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144

import exceptexception

print(type('some text')) <class str>
print(type(10))            <class int>
print(type(0.3))       <class float>
print(type(True))  <class bool>

beans_recipe = ['Soak beans in water', 'Dissolve salt in water', 'Heat water and beans to boil',
                'Drain beans when done cooking']

grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions',
 'rice', 'peppers', 'bananas']

def buy_groceries_individual(item_a=None,item_b=None,item_c=None,item_d=None,item_e=None):
    print('Buying %s...' % item_a)
    print('Buying %s...' % item_b)
    print('Buying %s...' % item_c)
    print('Buying %s...' % item_d)
    print('Buying %s...' % item_e)

efficent method
def buy_grocery_list(items):
    for item in items:
        print("buy items %s "item)

print(buy_grocies_indiviual
(grocery_a,grocery_b,grocery_c,grocery_d,grocery_e))
Buying chicken...
Buying onions...
Buying rice...
Buying peppers...
Buying bananas..

print(buy_grocies_list(grocery_list))

buy_grocies_individual(grocery_a,grocery_b,grocery_c)


grocery_f = 'squah'

buy_groceries_individual(grocery_a,
grocery_b, grocery_c, grocery_d, grocery_e, grocery_f)

short_grocery_list= ['chicken','onions','rice','peppers',
'bananas','squash']
buy_list_grocery(short_grocery_list)

output
Buying chicken...
Buying onions...
Buying rice...

long_grocery_list = ['chicken', 'onions',
                     'rice', 'peppers', 'bananas', 'squash']

print(buy_grocert(long_grocerty_list));

 output
 Buying chicken...
Buying onions...
Buying rice...
Buying peppers...
Buying bananas...
Buying squash...


list data structure

lists_of_lists = [['a','b','c'],[0,,1,2] ]
print(lists_of_lists)

lists = ['a','b','c','d']
print(lists)

output
[a,b,c,d]

grocery_a = 'chicken'
grocery_b = 'onins'
grocert_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

lists_of_lists = [ ['a','list','pf','words'],
                   [1,5,209], [True,True,False] ]

confusing_list = [ [23,73,50],'some words','12.308'[[False, True] ,'more words'] ]
 print(confusing_list)

************************************************************************************************
grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']

print(grocery_list)
print(grocert_list[2])

output
['chicken', 'onions', 'rice', 'peppers', 'bananas']
rice

print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])

chicken
onions
rice

print(grocery_list[-1]) #print the last element
print(grocert_list[0])  #prints the first element

print(grocery_list[1:4])
print(grocery_list[3:])
print)grocery_list{:3])

['onions', 'rice', 'peppers']
['peppers', 'bananas']
['chicken', 'onions', 'rice']

print(grocery_list[-1])
output
bananas
print(grocery_list[-3:])
['rice','peppers','bananas']

print(grocery_list)
['chicken', 'onions', 'rice', 'peppers', 'bananas']

print(grocery_list[::2])
['chicken', 'rice', 'bananas']
print(grocery_list[4:1:-1])
['bananas', 'peppers', 'rice']

printting all the elements of the list
for item in grocery_list:
    print(item)

chicken
onions
rice
peppers
bananas


for i in range(0,len(grocery_list),2):
    print(i,grocert_list[i])

output
0 chicken
2 rice
4 bananas


defitions of range functions
  range(start,end,step)


print(list(range(0,10,3)) )
print(list(range(104,100,-1)) )
print(list(range(5)) )

[0, 3, 6, 9]
[104, 103, 102, 101]
[0, 1, 2, 3, 4]


grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
output
['chicken', 'onions', 'rice', 'peppers', 'bananas']
grocery_list[-1] = 'oranges' # replace bananas with oranges
print(grocery_list)
output
['chicken', 'onions', 'rice', 'peppers', 'oranges']

grocery_list[1:3] = ['carrots', 'couscous'] #replace onions and rice with carrots and couscous
print(grocery_list)
['chicken', 'carrots', 'couscous', 'peppers', 'oranges']

****************************************************************************************************
append functions is used to append the values in the list
or else extend functions

grocery_list.append(['bread','salt'])
print(grocery_list)
output
['chicken', 'onions', 'rice',
'peppers', 'bananas', 'squash', 'bread', 'salt']

***********************************************************************************

Since lists can contain lists, we have to be careful
about adding multiple items to our list.
Instead of append, we might want to use extend.

grocery_list = ['chicken','onions','rice','peppers','banana','squash']
print(grocery_list)
grocery_list.extend(['bread','salt'] )
print(grocery_list)
***************************************************************
now using for loop

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']

for new_item in ['animesh','noble price']:
    grocery_list.append(new_item)

print(grocery_list)
*******************************************************************************************
deletes the last element from the list


del grocery_list[-1]
print(grocery_list)
['chicken', 'onions']
print(grocery_list)
print(grocery_list.pop(-1)) # last elements gets poped out fron the list

grocery_list.pop(0) #deletes the first element from the list

#sort the elements of the list

grocery_list.sort()

exercise

animesh = ['1','2','3','4','5','6','7','8','9','10']

select the last two elements
print(animesh[-2:])

elect every other element
starting with the second element.
print(animesh[2:])


"after copying the values of one variable into the another
but changes that are made in the orginal copy does reflect in the another"

note that it is not in the case of list

simply speaking
list call by reference
and varable call by value

a = 4
b = a
print(a,b) output 5 5
a = 5
print(a,b)  output 5 4


Tuple data structure

example_tuple = ('Dylan',26,167.7,True)
print(example_tuple)

('Dylam',26,267.7,True)

#error as the tuples value cannot be changed
print(example_tuple[2])
del example_tuple[-1]

def first_last(s):
    return s[0],s[-1]

 chars = first_last('hello!')
 print(chars)

output
h
!

name,age,height,has_dog = example_tuple
print(name)
print(age)
print(height)
print(has_dog)

output
Dylan
26
167.6
True

Gotcha

tup = tuple([ [] , 'a' ])
print(tup)
tup[0].append(1)
print(tup)

intial tuple = [ [],a ]
final tuple  = [ [1],a ]

set is same as list but it is unordered
and is immutable and has to have unique elements in it


example_set = {'Dylan', 26, 167.6, True}
print(example_set)

output
{True, 'Dylan', 26, 167.6}

"1.indexing not possible
2.set elements are not those that cannot be sliced similar to list"

however we can add delete the elements from the set template

example_set.add('True')
print(example_set)
example_set.update([58.1,'brown'] )

output
{167.6, 'Dylan', 'True', 26}
{'brown', 58.1, 167.6, 'Dylan', 'True', 26}

note set elements are helpful to find the elements faster

piles = [2.83, 8.23, 9.38, 10.23, 25.58, 0.42, 5.37, 28.10, 32.14, 7.31]

def hash_functions(x):
    return int(x*100 % 31)

[hash_functions(pile) for pile in piles]
ouput
[4, 17, 8, 0, 16, 11, 10, 20, 21, 18]


print(int(5.37 * 100 % 31))
10


print(set([23, 609, 348, 10, 5, 23, 340, 82]))
print(set(('a', 'b', 'q', 'c', 'c', 'd', 'r', 'a')))

output
{609, 5, 10, 82, 340, 23, 348}
{'b', 'a', 'd', 'c', 'q', 'r'}


student_a_courses = {'history', 'english', 'biology', 'theatre'}
student_b_courses = {'biology', 'english', 'mathematics', 'computer science'}

print(student_a_courses.intersection(student_b_courses))
output:  english

print(student_a_courses.union(student_b_courses))
output:
history,english,biology,thetre,mathematics,computer science
print(student_a_courses.difference(student_b_courses))
 output:
  history, biology ,theatre
print(student_b_courses.difference(student_a_courses))
  output:
    mathematics,computerscience
print(student_a_courses.symmetric_difference(student_b_courses))
  output

*****************************************************************************************************

dictionary

me = ['Dylan',28,167.7,56.5,'brown',True]

print('my name is %s',%me[0])
print('I have %s hair'%me[4])

me_dict = {'name': 'Dylan',
            'age': 28,
            'height': 167.5,
            'weight': 56.5,
            'hair': 'brown',
            'eyes': 'brown',
            'has dog': True  }

print('My name is %s' % me_dict['name'])
print('I have %s hair' % me_dict['hair'])
My name is Dylan
I have brown hair

#ZIP the dictionary

value_list = me
key_list = ['name',
'age',
'height',
'weight',
'hair'
,'eyes',
'has dog']

print(value_list)
print(key_list)

#joining the first and the second value

key_value_pairs = list(zip(key_list,value_list))
print(key_value_pairs)


#converting to dict

me_dict = dict(key_value_pairs)
print(me_dict)

me_dict = {'name': 'Dylan',
            'age': 28,
            'height': 167.5,
            'weight': 56.5,
            'hair': 'brown',
            'eyes': 'brown',
            'has dog': True  }


%%expect_exception TypeError

# this doesn't work because the list cannot have the duplicate values
invalid_dict = {[1, 5]: 'a', 5: 23}

dictionary elements are immuatable and cannot have duplicate values

valid_dict = {(1,5):'a' , 5:[23,6] }
print(IN_valid_dict)

replacing the value in the dictionary

me_dict['favourite book'] = 'animesh Noble price'
print(me_dict)

me_dict = {'name': 'Dylan',
            'age': 28,
            'height': 167.5,
            'weight': 56.5,
            'hair': 'brown',
            'eyes': 'brown',
            'has dog': True
            'favourite book':'animesh Noble price'
            }


me_dict.update({'favorite color': 'orange',
                'siblings': 3, 'nieces/nephews': 3})


print(me_dict)
me_dict = {'name': 'Dylan',
            'age': 28,
            'height': 167.5,
            'weight': 56.5,
            'hair': 'brown',
            'eyes': 'brown',
            'has dog': True
            'favourite book':'animesh Noble price',
             'favourite color':'orange'
             'siblings':3,
             'nieces':3
            }
Replace the key values of the dictionary

print(me_dict)
me_dict['nieces'] = 4
print(me_dict)

me_dict = {'name': 'Dylan',
            'age': 28,
            'height': 167.5,
            'weight': 56.5,
            'hair': 'brown',
            'eyes': 'brown',
            'has dog': True
            'favourite book':'animesh Noble price',
             'favourite color':'orange'
             'siblings':3,
             'nieces':4
            }

del me_dict['favourite book']
deleted the favourite from the dictionary

print(me_dict.pop('siblings'))
print(me_dict)

# to display the value of the dictionary items

print(me_dict.keys())
print(me_dict.values())
print(,e_dict.items())


searching in the dictionary

print('hair' in me_dict) True
print('has cat' in me_dict) True
print('brown' in me_dict)  True

if 'has dog' in me_dict:
    print('has dog: %s' %me_dict['has dog] )
else:
    print(None)

if 'has_cat' in me_dict:
    print('Has cat:%s'%me_dict['has_cat'])
else:
    print(None)

get method is used to search the values in the dicitonary

print('Has dog: %s' %me_dict.get('has dog'))
print('Has cat: %s' %me_dict.get('has cat'))


print(sorted(map(str,example_tuple)   ))
print(sorted(map(str,example_set) ))
print(sorted(me_dict.items() ))
print(sorted(me_dict))

iterations

for k in me_dict:      #prints the key elements of the dictionary
    print(k)

#prints the dict[key] of the dictionary elements
for k,v in me_dict.items():
    print('%s : %s'%(k,v))


square = [x**2 for x in range(10)]
square_lut = [x:x**2 for x in range(10)]

print(square)
print(square_lut)

me_dict_dtypes = {k:type(v) for k,v in me_dict.items()}
print(me_dict_dtypes)

square_lut = {}
for x in range(10):
    square_lut[x] = x**2
print(square_lut)

comprehensive way
square_lut = {x:x**2 for x in range(10)}
print(square_lut)

namedtuple

from collections import namedtuple
Vector3 = namedtuple('Vector ',['x','y','z'])

default dict used to count the freq in the dictionary

def count(x):
    count_dict = {}
    for ele in x:
        if ele in count_dict.keys():
            count_dict[ele] += 1
        else:
            count_dict[ele] = 1
     return count_dict
#function calling the count_defalt functions
 count(ele)

**********************************************************************************************

from collections import defaultdict
def count_default(x):
    count_dict = defaultdict(int)
    for ele in x:
        count_dict[ele] += 1
    return count_dict
 #function calling the count_defalt functions
count_default(ele)

*********************************************************************************

deque

from collections import deque

d = deque([2,3,4,5])
print(d)
d.append(10)
print(d)
d.appendleft(20)
print(d)

To calcuate the time complexity

%%timeit
l_ = list()
for i in range(40000):
    l_.insert(0,i)


















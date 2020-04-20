###########python intro
###########python intro
a = 5
print(a)

def mult(a):
    for x in range(len(a)):
        return a[x]*10

mult([3,2,3])

##########program flow

 1+1

2 * 3.5

1 + 1
2 * 3.5
print(1 + 1)
print(2 * 3.5)

print('1 + 1 is', 1 + 1)
# this is a comment, Python won't try to execute it
print('All done!')

first_result = 1 + 1
final_result = first_result * 3.5
print(final_result)


my_name = 'Dylan'
my_age = 28
my_favorite_number = 2.718
has_dog = true

print(my_name)
print(my_age)
print(my_favourite_number)
print(has_dog)

now to check the type of each data type;

print(type(my_name))
print(type(my_age))
print(type(my_favoutrite_number))
print(type(has_dog))

execise
1.
my_name = 'animesh'
my_age = 18
print(my_name)
print(my_age)

2.
my_name = "animesh Ram"
my_age = 18
print(my_name)
print(my_age)

my_age = my_age+10
print(my_age)
print("my age after the 10 yrs".format(my_age))

functions

def square(number):
    return number**2

squared = square(5.5)
print(squared)

my_number = 6
print(square(my_number) )
#now not all values are valid input in the functions
%%expect_exception TypeError
print(square('banana'))

exercise 2:

    def cube(number):
        return number**3

    cube(3)

assert functions is used for checking wheather the  calculated in the right value or not
assert cube(3) == 27
assert cube(3) == 26
# since the above value is the wring value hence


 def say_hello(name):
     print("hello {}".format(name))

 say_hello('animesh')

 output : hello animesh

#why functions are used

def do_it(x):
    print(x**2+2)

do_it(1)
do_it(2)
do_it(3)
do_it(4)
do_it(5)
do_it(6)
do_it(7)
do_it(8)
do_it(9)

def do_it(x):
    print( (x**2+2)**2 )

do_it(1)

syntax

def example_a():
    print('example is running ')
    print('returing value of a')
    return a;
    print('this will not exercises')

 example_a()

 def example_b():
     print("examaple is running ")
     print('existing without retunring a value')

example_b()

Conditionals and logic

def testing_high_score(player_1,high_score):
    if player_score > high_score:
        print('high score')
        high_score - player_score
     return high_score

print(testing_high_score(83,98))
98
print(testing_high_score(95,93) )
High score
95

def nested_example(x):
    if x<50:
        if x%2 == 0:
            return 'branch a'
        else:
            return 'branch b'
        else:
            return 'branch c'

print(nested_example(42))
print(nested_example(51))
print(nested_example(37))

output
branch a
branch c
branch b

print(50 > 10) true
print(2+2 == 4) true
print(-3 > 2)  false

print(True and True)
print(True and False)
print(False and True)
print(False and False)
output
True
False
False
False

x = 5
y = 3

print(x>4 and y>2)  true
print(x>7 and y>2)  false
print(x>7 and y>2)  true

print(not true) false
print(not false) true

x = 10
y = 8
print(x > 7 or y < 7) true
print(not x > 7 or y < 7) false
print(not x > 7 or not y < 7) true
print(not (x > 7 or y < 7)) false

def exercide_1(n):

    if(n> 10 and n<20) or n<-100:
        return True
    return False

exercise_1(11) true

##########iterations

x = 0
while x < 5:
    print(x)
    x = x + 1

    output
0
1
2
3
4

def first_n_fibanacci(n):
    prev_num = 0
    curr_num - 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count<= n:
        next_num = prev_num+curr_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

#doubt in the program of below the fibbo

def below_x_fibonacci(x):
    prev_num = 0
    curr_num = 1

    if curr_num <x:
        print(prev_num)
        print(curr_num)
    elif prev_num<x:
        print(prev_num)

    while curr_num



bread_recipe =
 ['Dissolve salt in water', 'Mix yeast into water', 'Mix water with flour to form dough',
                'Knead dough', 'Let dough rise', 'Shape dough', 'Bake']


soup_recipe = ['Dissolve salt in water', 'Boil  water', 'Add bones to boiling water', 'Chop onions',
               'Chop garlic', 'Chop carrot', 'Chop celery', 'Remove bones from water',
               'Add vegetables to boiling water', 'Add meat to boiling water']

beans_recipe = ['Soak beans in water', 'Dissolve salt in water', 'Heat water and beans to boil',
                'Drain beans when done cooking']


def print_recipe(inst):
    for step in inst:
        print(step)

print_recipe(soup_recipe)

output

Dissolve salt in water
Boil water
add bones to boiling water
chop onins
chop garlic
chop carrot
chop celery

def first_n_fibonacci_while(n):
    prev_num =0
    curr_num =1
    count = 2

    print(prev_num)
    print(curr_num)

    while count<n:
        next_num = curr_num_prev_num
        print(next_num)
        prev_num = curr_num
        curr_num =  next_num
        count +=1

first_n_fibonacci_while(7)


 for loop method 3:

     def  first_fibo_using_for_loops(7):
         prev_num = 0
         curr_num = 1

         print(prev_num)
         print(curr_num)

         for count in range(2,n+1):
             next_num = prev_num+curr_num
             print(next_num)
             prev_num = curr_num
             curr_num = next_num

 first_fibo_using_for_loops(7)


def is_prime(number):
    if number<2:
        return False

    for factor in range(2,number):
        if number%factor == 0:
            return False

     return True

def print_prime(n):
    for number in range(1,n):
        if if_prime(number):
            print("%d id primt"% number)

print_prime(42)
output
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime

list_of_numbers = [0, 1, 2, 3, 4, 5,
6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
prime_list = []

for number in list_of_numbers:
    if is_primt(number):
        primt_list.append(number)
print(prime_list)

awesome comphredions

[number for number in list_of_number if is_prime(number)]
[2, 3, 5, 7, 11, 13, 17, 19]

def print_thid(a):
    print('inside print this')

a = 5
print_this(2)
print('a = ',a)



global and local variable

def print_this(a):
    print('inside print this',a)

a = 5
print_this(2)
print('a = ',a)

output
2

note
#but when  nothing is passed in the functions
#it takes the global variable
def print_this():
    print('inside print it',a)

a = 5
print_it()
print('a = ',a)

output
5

def some_exponent(exponent):
    def func(x):
        return x**exponent
    return func

some_exponent(2)(2)

def print_tode(watch_tv,read,eat,sleep):
    print('i need to')
    if watch_tv:
        print('watch tv')
    if read:
        print('read')
    if eat:
        print('eat')
    if sleep:
        print('sleep')
print_todo(True,True,True,True)

I need to:
  watch_tv
  read
  eat
  sleep

def print_todo_default(watch_tv,read,eat,sleep):
    print("I need to")
    if watch_tv:
        print('watch_tv')
    if read:
        print('read')
    if eat:
        print('eat')
    if sleep:
        print('sleep')
print_todo_default(True,True)

output
I need to:
  watch_tv
  read
  eat
  sleep

note
  very important as we donot know how arguments to pass then we use this


def print_todo_args(*args):
    print('I needed to ')
    for arg in args:
        print(' '+arg)

print(print_tode_args('watch_tv','read'))




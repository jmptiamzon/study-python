#if elif
if 0 < 5:
    print('hello')
elif 1 > 4:
    print('hello1')
else:
    print('')

#loop
print('My name is ')
for i in range(5):
    print('Jimmy Five Times ' + str(i))


for i in range(1, 5):
    print(i)


for i in range (0, 11, 2):
    print(i)


#from random import *
import random, sys, os, math

random.randin(1, 10)


#def block
def testDef():
    print('1')
    print('2')
    print('3')

test(def)

def testDef1(number):
    print(str(number))

testDef1(3)

def testDef2(number)
    return number + 1

myNum = testDef2(1)
print(myNum)

#remove line break
print('Hello', end='')

#print multiple string in single line
print('Hello', 'World!')
print('Hello', 'World', sep='_')


#global vs local scopes

def test3():
    # if you want to use the global var ones
    # global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
test3()
print(eggs)

#try except
def divByZero(val):
    try:
        return 42 / val
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(divByZero(0))

def divByZero():
    val = input()

    try:
        if int(val) > 3:
            print('Value greater than 3')

        else:
            print('Value less than 3')


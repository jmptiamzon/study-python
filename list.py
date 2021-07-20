myList = ['a', 'b', 'c']

#to access
print(myList[0])

#to access reverse
print(myList[-1])

myList[['a', 'b', 'c'], [1, 2, 3, 4]]

print(myList[0][1])

#slice
myList = ['a', 'b', 'c', 'd']

print(myList[1 : 3]) #start at index 1 not including index 3

myList[1 : 3] = ['e', 'f', 'g', 'h']

print(myList[:2]) #starting at index 0 to not including index 2
print(myList[1:]) #start at index 1 until end

del myList[1] #remove index 1

#length
print(len('Hello')) #5

print(len[1,2,3]) #3

print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6]

print('Hello' * 3) #HelloHelloHello

print(list('Hello')) #['H', 'e', 'l', 'l', 'o']

'a' in ['a', 'b', 'c'] #True
'a' not in ['a', 'b', 'c'] #False



#loop

for i in range(4)
    print(i)

#can do this
for i in [0, 1, 2, 3]:
    print(i)

list(range(0, 100, 2)) #start at 0, end at 100 not including 100, skip 2


myList = ['a', 'b', 'c']

for i in range(len(myList)):
    print(myList[i])


#multiple assignment

a, b, c = ['a', 'b', 'c']
a, b, c = 'a', 'b', 'c'

a = 'aaa'
b = 'bbb'

a,b = b,a

#index method
myList = ['a', 'b', 'c']
myList.index('a') #0
myList.index('d') #will throw exception

myList = ['a', 'a', 'b', 'c']
myList.index('a') #0 will return the first occurrence

#append method
myList = ['a', 'b', 'c']
myList.append('d') #['a', 'b', 'c', 'd']

#insert method
myList = ['a', 'b', 'c']
myList.insert(1, 'b') #['a', 'b', 'b', 'c']

#remove and delete
myList = ['a', 'b', 'c']
myList.remove('a') #if not in list will throw exception

del myList[0]

#sort method
myList = [3, 2, 1]
myList.sort() #[1, 2, 3]

myList = [1, 'a', 3, 4]
myList.sort() #will throw exception

#if you sort with upper case and lower case, upper case will be prioritized / asciibetical order

#to change to alphabetical order
myList = ['A', 'B', 'C', 'a', 'b', 'c']
myList.sort(key=str.lower)

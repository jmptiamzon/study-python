import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-999'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group()) # will only get first occurrence

mo = phoneNumRegex.findall(message) # will get all occurrences
print(mo) 


#grouping
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search(message)
mo.group() # first occurrence number
mo.group(1) # first bracket
mo.group(2) # second bracket


#how to get paranthesis
message = '(415) 555-4242'
phoneNumRegex = re.compile(r'\(\d\d\d) \d\d\d-\d\d\d')
mo.group()


#pipe |
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group() # Batmobile
mo.group(1) # mobile

mo = batRegex.search('Batmotorcycle')
mo.group() #will throw error since mo == None


#===================================================
# ? pattern
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
mo.group() #Batwoman

mo = batRegex.search('The Adventures of Batwowowowowoman')
mo.group() # mo == None

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 123-1234') #True
phoneRegex.search('My phone number is 123-123-1234') #True

# * pattern
batRegex = re.compile(r'Bat(wo)*man')
batRegex.search('Batwoman') # True
batRegex.search('Batman') #True
batRegex.search('Batwowowowowoman') #True

# + pattern
batRegex = re.compile(r'Bat(wo)+man')
batRegex.search('Batwoman') #True
batRegex.search('Batman') #False

#define number of repetition
haRegex = re.compile(r'(Ha){3}') #should appear 3 times
mo = haRegex.search('HaHaHa') #True

haRegex = re.compile(r'(Ha){3,5}') #min of 3, max of 5 if more will return first 5 | if {,5} 0 or more
haRegex.search('HaHaHa')

digitRegex = re.compile(r'(\d){3,5}') #greedy match | will return longest match in string
digitRegex.search('12345678') #will return 12345 because pyhton in default uses greedy match

digitRegex = re.compile(r'(\d){3,5}?') #non greedy | will return shortest match in string
digitRegex.search('1234567') # will return 123


#findall() | if it has groupings () it will get by group or tuples
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.findall('123-123-1234 567-891-0123') #['123-123-1234', '567-891-0123']

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneRegex.findall('123-123-1234 567-891-0123') #[('123', '123-1234'), ('567', '891-0123')]

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phoneRegex.findall('123-123-1234 567-891-0123') #[('123-123-1234', '123', '123-1234'), ('567-891-0123', '567', '891-0123')]


#create own character class
vowelRegex = re.compile(r'[aeiou]') #[a-z]{2} 2 letters
consonantRegex = re.compile(r'[^aeiou]') # not in the brackets


beginsWithHelloRegex = re.compile(r'^Hello') #string should start with Hello
endsWithWorldRegex = re.compile(r'world!$') #$ means end of string

allDigitsRegex = re.compile(r'^\d+$') #begins and end with digit

atRegex = re.compile(r'.at') # dot is any chars
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') 
#(.*) greedy match (.*?) non greedy match
nameRegex.findAll('First Name: Al Last Name: Sweigart') #will return both groups since greedy

nongreedy = re.compile(r'<(.*?)>')
serve = '<To serve humans> for dinner'
nongreedy.findAll(serve) # will return To serve humans only

#.* doesnt match / get \n to get \n in the string we need to use
dotStar = re.compile(r'.*', re.DOTALL)

#if you dont want to type capital letter
doStar = re.compile(r'.*', re.IGNORECASE) #or re.I


namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.findAll('Agent Alice gave the secret documents to Agent Bob.') #['A', 'B']
namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
#\1 here will get the first group
#Agent A**** ......

#VERBOSE to make regex more readable
re.compile(r'''
(\d\d\d-)|     #area code (without parens)
(\(\d\d\d))    # or area code with parens no dash
\d\d\d      #first 3 digits
-           #second dash
\d\d\d\d    # last 4 digits
\sx\d{2,4}  # extension, like x1234
''', re.VERBOSE | re.DOTALL | re.IGNORECASE) #to use multiple options










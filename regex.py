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





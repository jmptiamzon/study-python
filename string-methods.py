#lower & upper | this doesn't change the string itself
test = 'Ok'

print(test.lower()) #ok
print(test.upper()) #OK


#isupper() & islower() | change the actual string

test = 'Ok'
test.isupper()

print(test) #OK

test.islower()

print(test) #ok


#isalpha() - chekc if letters only
#isalnum() - check if alphanumeric
#isdecimal() - chekc if numbers only
#isspace() -check if whitespace only
#istitle() - check if titlecase only

','.join(['cats', 'rats', 'bats']) #'cats,rats,bats'
'hello world'.titlte() #Hello World
'hellow word'.istitle() #False
'Hello World'.startswith('ello') #False
'Hello World'.endswith('World') #True

'Hello World'.split() #['Hello', 'World']
'Hello World'.split('l')


#ljust() & rjust() | justify
'Hello'.rjust(10) #insert leading space 10
'Hello'.ljust(10) #insert trailing space 10
'Hello'.ljust(10, '#') #insert # instead of space

'Hello'.center(10) #put leading and trailing space
'Hello'.center(10, '#') # insert # instead of space


#strip() & rstrip() & lstrip() | remove spaces
test = 'Hello'.rjust(10)
test = test.strip() #remove leading and trailing

'test@test'.strip('@')
'test   '.rstrip()
'   test'.lstrip()


#replace
test = 'Hello'
test.replace('e', 'ABC')

#pip.exe install pyperclip

# pyperclip is used to copy and paste using clipboard (ctrl + c , ctrl + v)
import pyperclip
pyperclip.copy('Hello')
pyperclip.paste() #'Hello'



test


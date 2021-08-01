import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

#use triple quotes ''' to escape everythin in a giant string

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#print(count)
pprint.pprint(count) #pretty print

#if you want to save the print values
#textStr = pprint.pformat(count)

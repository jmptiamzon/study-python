#! pyhton3

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  #area code (optional)
(\s|-)  #separator
\d\d\d  #first three digits
-       #separator
\d\d\d\d  #last four digits
(((ext(\.)?\s)|x)  #extension
(\d{2,5}))?
)

''', re.VERBOSE)


# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+ #name
@
[a-zA-Z0-9_.+]+ #domain name
''', re.VERBOSE)



# TODO: Get the text off the clipboard
text = pyperclip.paste()



# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

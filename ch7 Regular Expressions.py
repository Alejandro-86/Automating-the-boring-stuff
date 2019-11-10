import re
import pyperclip


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
     [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    aux = re.sub('[(){}<>]', '', groups[1])
    phonenum = '-'.join([aux, groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    matches.append(phonenum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

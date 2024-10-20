'''
1. Get the text off the clipboard
2. Find all phone numbers and email addresses in the text.
3. paste them onto the clipboard
'''

#! python3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboard.

import pyperclip, re

# Regex pattern for finding US phone numbers.
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # separator
                        (\d{3})                         # first 3 digits
                        (\s|-|\.)                       # separator
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # last 4 digits
                        )''', re.VERBOSE)

# Regex pattern for finding email addresses.
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+   # username
                        @                   # @ symbol
                        [a-zA-Z0-9.-]+      # domain name
                        (\.[a-zA-Z]{2,4})   # dot-something
                        )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
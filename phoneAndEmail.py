'''
1. Get the text off the clipboard
2. Find all phone numbers and email addresses in the text.
3. paste them onto the clipboard
'''

#! python3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboard.

import pyperclip, re
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # separator
                        (\d{3})                         # first 3 digits
                        (\s|-|\.)                       # separator
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # last 4 digits
                        )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
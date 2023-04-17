# Write your code here

import re

def  is_valid_password(string):
    allowed = [
        r'.{12,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',
    ]
    not_allowed = [r'(.)\1{2}',r'(.)(.*\1){3}']
    
    return all(re.search(regex, string) for regex in allowed) and not any(re.search(regex, string) for regex in not_allowed)
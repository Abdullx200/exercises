# Write your code here

import re
def replace(string):
    return '*' * len(string.group(0))

def hide_email_addresses(string):
    return re.sub(r'([a-zA-Z0-9.]+@[a-zA-Z0-9.]+)',replace,string, flags= re.MULTILINE)
# Write your code here
import re

def parse_link(string):
    match = re.fullmatch(r'<a href="(.+)">(.+)</a>', string)
    if match:
        caption = str(match.group(2))
        link = str(match.group(1))
        herf = (caption, link)
        return herf
    
    else:
        return None
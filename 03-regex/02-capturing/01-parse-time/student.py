import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        miliseconds = 000
        
        if match.group(4):
            miliseconds = int(match.group(4))
        
        time = (hours, minutes, seconds, miliseconds)
        return (time)
    
    else:
        return None

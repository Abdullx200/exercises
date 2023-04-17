# Write your code here
import re

def three_to_ten_times_abc(string):
    return re.match("(abc){3,10}",string)
# Write your code here


def last_digit(x):
    return x%10
def remove_last_digit(x):
    return x//10


def digit_sum(x):
    s = 0
    s += last_digit(x)
    while x>0:
        remove_last_digit(x)
        s+=last_digit(x)
    return s

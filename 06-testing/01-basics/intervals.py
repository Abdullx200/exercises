"""def overlapping_intervals(interval1 = tuple, interval2 = tuple):
    overlap = False
    begin,einde = interval1
    b, e = interval2
    for i in range(begin, einde+1):
        if b==e==begin==einde:
            overlap = True
            return overlap
        elif b != begin and e==einde:
            return overlap 
        #????
        elif i in interval2:
            overlap = True
        
    return overlap"""

def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2
    
    if left1 > right1 or left2 > right2:
        return False
    
    if left1 == right1:
        return left1 >= left2 and left1 <= right2
    
    if left2 == right2:
        return left2 >= left1 and left2 <= right1
    
    return left1 <= right2 and left2 <= right1

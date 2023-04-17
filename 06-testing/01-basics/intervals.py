def overlapping_intervals(interval1,interval2):
    overlap = False
    for i in range(interval1):
        if i in interval2:
            overlap = True
    return overlap
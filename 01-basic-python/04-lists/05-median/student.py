# Write your code here

def median(ns):
    ns.sort()
    if len(ns)%2 != 0:
        return ns[(len(ns)-1)//2]
    elif len(ns) == 2:
        return sum(ns)/2
    else:
        return (ns[(((len(ns))//2)+1)] + ns[(((len(ns))//2)-1)])/2
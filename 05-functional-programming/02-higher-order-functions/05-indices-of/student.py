def indices_of(xs, condition):
    l = []

    for index in range(len(xs)):
        if condition(xs[index]):
            l.append(index)
        
    return l